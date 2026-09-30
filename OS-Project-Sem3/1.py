# ASSIGNMENT 1: CPU SCHEDULING
# FCFS, SJF, SRTF, Priority, Round Robin and DAPS
processes = [
    {'pid':'P1','at':0,'bt':6,'priority':2},
    {'pid':'P2','at':1,'bt':4,'priority':1},
    {'pid':'P3','at':2,'bt':2,'priority':3},
    {'pid':'P4','at':3,'bt':3,'priority':2}
]
def metrics(ps, g):
    ans = {}
    for p in ps:
        pid=p['pid']; first=None; ct=0
        for a,b,x in g:
            if x==pid:
                if first is None: first=a
                ct=b
        tat=ct-p['at']; wt=tat-p['bt']; rt=first-p['at']
        ans[pid]=(ct,tat,wt,rt)
    return ans
def show(ps,g):
    r=metrics(ps,g)
    print('\nGantt:')
    print(' '.join(f'|{x}:{a}-{b}' for a,b,x in g)+'|')
    for p in ps:
        print(p['pid'], 'CT=',r[p['pid']][0], 'TAT=',r[p['pid']][1],
              'WT=',r[p['pid']][2], 'RT=',r[p['pid']][3])
    n=len(ps)
    print('Avg TAT =',round(sum(x[1] for x in r.values())/n,2))
    print('Avg WT  =',round(sum(x[2] for x in r.values())/n,2))
    print('Avg RT  =',round(sum(x[3] for x in r.values())/n,2))
    print('Context switches =',sum(g[i][2]!=g[i-1][2] for i in range(1,len(g))))
def fcfs(ps):
    time=0; g=[]
    for p in sorted(ps,key=lambda x:(x['at'],x['pid'])):
        time=max(time,p['at']); g.append((time,time+p['bt'],p['pid'])); time+=p['bt']
    return g
def sjf(ps):
    time=0; done=set(); g=[]
    while len(done)<len(ps):
        r=[p for p in ps if p['pid'] not in done and p['at']<=time]
        if not r: time+=1; continue
        p=min(r,key=lambda x:(x['bt'],x['at'],x['pid']))
        g.append((time,time+p['bt'],p['pid'])); time+=p['bt']; done.add(p['pid'])
    return g
def preemptive(ps,key):
    rem={p['pid']:p['bt'] for p in ps}; time=0; done=0; g=[]
    while done<len(ps):
        r=[p for p in ps if p['at']<=time and rem[p['pid']]>0]
        if not r: time+=1; continue
        p=min(r,key=lambda x:key(x,rem[x['pid']]))
        if g and g[-1][2]==p['pid']: g[-1]=(g[-1][0],time+1,p['pid'])
        else: g.append((time,time+1,p['pid']))
        rem[p['pid']]-=1; time+=1
        if rem[p['pid']]==0: done+=1
    return g
def srtf(ps):
    return preemptive(ps,lambda p,r:(r,p['at'],p['pid']))
def priority(ps):
    return preemptive(ps,lambda p,r:(p['priority'],p['at'],p['pid']))
def rr(ps,q=2):
    ps=sorted(ps,key=lambda x:x['at']); rem={p['pid']:p['bt'] for p in ps}
    qlist=[]; i=0; time=0; done=0; g=[]
    while done<len(ps):
        while i<len(ps) and ps[i]['at']<=time: qlist.append(ps[i]); i+=1
        if not qlist: time=ps[i]['at']; continue
        p=qlist.pop(0); pid=p['pid']; run=min(q,rem[pid]); g.append((time,time+run,pid)); time+=run; rem[pid]-=run
        while i<len(ps) and ps[i]['at']<=time: qlist.append(ps[i]); i+=1
        if rem[pid]>0: qlist.append(p)
        else: done+=1
    return g
def daps(ps,q=2,alpha=.5):
    rem={p['pid']:p['bt'] for p in ps}; time=0; done=0; g=[]
    while done<len(ps):
        r=[]
        for p in ps:
            pid=p['pid']
            if p['at']<=time and rem[pid]>0:
                wait=time-p['at']-(p['bt']-rem[pid])
                score=rem[pid]+p['priority']-alpha*wait
                r.append((score,p['at'],pid,p))
        if not r: time+=1; continue
        p=min(r,key=lambda x:(x[0],x[1],x[2]))[3]; pid=p['pid']; run=min(q,rem[pid])
        g.append((time,time+run,pid)); time+=run; rem[pid]-=run
        if rem[pid]==0: done+=1
    return g
for name,fn in [('FCFS',fcfs),('SJF',sjf),('SRTF',srtf),('Priority',priority)]:
    print('\n===',name,'==='); show(processes,fn(processes))
print('\n=== Round Robin ==='); show(processes,rr(processes,2))
print('\n=== DAPS ==='); show(processes,daps(processes,2,.5))
