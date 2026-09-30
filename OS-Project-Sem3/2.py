# ASSIGNMENT 2: REAL-TIME SCHEDULING
# RMS, EDF and SAFS
from math import gcd
tasks=[
    {'id':'T1','c':1,'period':4,'deadline':4},
    {'id':'T2','c':2,'period':6,'deadline':6},
    {'id':'T3','c':3,'period':8,'deadline':8}
]
def lcm(a,b): return a*b//gcd(a,b)
def hyperperiod(ts):
    h=1
    for t in ts: h=lcm(h,t['period'])
    return h
def jobs(ts,limit):
    out=[]
    for t in ts:
        r=0; k=1
        while r<limit:
            out.append({'task':t['id'],'job':k,'release':r,'rem':t['c'],
                        'deadline':r+t['deadline'],'period':t['period']})
            r+=t['period']; k+=1
    return out
def simulate(ts,rule,limit):
    js=jobs(ts,limit); time=0; g=[]; misses=[]
    while time<limit:
        for j in js:
            if j['rem']>0 and j['release']<=time and j['deadline']<=time and j not in misses:
                misses.append(j)
        ready=[j for j in js if j['release']<=time and j['rem']>0 and j not in misses]
        if not ready:
            g.append((time,time+1,'IDLE')); time+=1; continue
        j=min(ready,key=lambda x:rule(x))
        if g and g[-1][2]==j['task']: g[-1]=(g[-1][0],time+1,j['task'])
        else: g.append((time,time+1,j['task']))
        j['rem']-=1; time+=1
        if j['rem']==0: j['completion']=time
    return js,g,misses
def rms(j): return j['period']
def edf(j): return j['deadline']
def safs(j): return j['deadline']-j['rem']
def show(name,js,g,misses,limit):
    print('\n===',name,'===')
    print('Gantt:',' '.join(f'|{x}:{a}-{b}' for a,b,x in g)+'|')
    for j in js:
        status='MISS' if j in misses else 'MEET'
        ct=j.get('completion','-')
        print(j['task']+'-'+str(j['job']), 'Release=',j['release'],
              'Deadline=',j['deadline'], 'Completion=',ct, status)
    idle=sum(b-a for a,b,x in g if x=='IDLE')
    busy=limit-idle
    print('Busy time =',busy)
    print('Idle time =',idle)
    print('CPU utilization =',round(busy/limit*100,2),'%')
    print('Deadline misses =',len(misses))
H=hyperperiod(tasks)
print('Hyperperiod =',H)
U=sum(t['c']/t['period'] for t in tasks)
print('CPU utilization =',round(U*100,2),'%')
for name,rule in [('RMS',rms),('EDF',edf),('SAFS',safs)]:
    js,g,m=simulate(tasks,rule,H)
    show(name,js,g,m,H)
