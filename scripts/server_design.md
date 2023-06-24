
https://app.diagrams.net/#Hsimugongzi%2FServerDoc%2Fmain%2FServer.drawio
https://www.lanindex.com/%e6%89%8b%e6%b8%b8%e5%8c%b9%e9%85%8d%e6%9c%8d%e5%8a%a1%e5%99%a8%e8%ae%be%e8%ae%a1%e6%80%bb%e7%bb%93/
https://www.jianshu.com/p/47388604a64f
https://cloud.tencent.com/developer/article/1050729
--------------------------------------------------------------------------

pip install kbengine_tips


try:
    import KBEngine
except ImportError:
    from kbengine_tips.BaseApp import KBEngine


技能由武器的内部配置组合而成;人物有天赋和属性
生活技能没有数值 只有冷淡 一般 喜爱种田

战斗被扑倒 倒地状态收到近战伤害增加
--------------------------------------------------------------------------

DEBUG_MSG('simu  xx (%s) ' % (   ))
WARNING_MSG("SIMU test  ")
TRACE_MSG("SIMU test  ")
INFO_MSG("SIMU test  ")
WARNING_MSG("SIMU test  ")
ERROR_MSG("SIMU test  ")

---------------------------

###Python命令行调试游戏逻辑例子(在Python命令行输入):

查看当前进程上的所有Entity:
KBEngine.globalData.items()
KBEngine.entities.items()
[1: Space at 0x4D3040, 2: Monster at 0x4D3038]

KBEngine.entities[44].__dict__

KBEngine.entities.items()
KBEngine.entities[9]
KBEngine.entities[9].base
KBEngine.entities[9].base.cell.teleportSpace
KBEngine.globalData.items()
KBEngine.globalData["Spaces"]

for entityID, entity in KBEngine.entities.items(): print("entityID:%i, entity=%s",(entityID,entity))
1, Space at 0x4D3040
2, Monster at 0x4D3038
查看Entity当前的坐标:

KBEngine.entities[entityID].position
(10.0, 0, 10.0)
改变Entity的朝向:

KBEngine.entities[entityID].direction.z = math.pi
调用Entity的接口:

KBEngine.entities[entityID].funcXXX()
手动创建一个Entity(cellapp):

e = KBEngine.createEntity("Monster", spaceID, (10.0, 0, 10.0), (0.0, 0, 0.0), {})
调用一个Entity的远程方法(cellapp):

KBEngine.entities[entityID].base.func()
KBEngine.entities[entityID].client.func()

--------------------------------------------------------------------------
、
ALL_CLIENT 属性能被周围的客户端获得，包括自身。相当于同时设置了OWN_CLIENT和OTHER_CLIENT标志。
ALL_CLIENTS 同ALL_CLIENT
BASE 只能在Base上使用
BASE_AND_CLIENT 属性在base和客户端都可见，相当于同时设置了OWN_CLIENT和BASE标志。
CELL_PRIVATE entity的内部属性。 只在cell的entity内部可见，相当于私有属性。
CELL_PUBLIC 可以被服务端的其它entity访问。在kbe中，现在暂时和CELL_PUBLIC是一样的。
CELL_PUBLIC_AND_OWN 在cell上的其它entity可见，对客户端来说，仅自身客户端可见

baseapp的属性改变只会发给自己的客户端，而不会广播
cellapp有广播的可能

--------------------------------------------------------------------------

SpaceAlloc创建普通space--大世界场景，服务器开启就创建。spacekey和属性都通过固定类型来指定。
SpaceAllocDuplicate副本为SpaceAlloc的派生，按需生成，使用特定的spacekey和属性来创建space

假如用户在某个space掉线？---临时副本有时间限制或者逻辑现在，会销毁，若无销毁则尝试进入。

--------------------------------------------------------------------------


crriter{
	Combat : propertys   
	skill
	motion/navigate
	state
	AI

}




cell battle mode
{






Avatar的cell创建的时候 在space中创建队员 队员具有AI并由服务器控制 但是ai中优先执行avatar客户端发送的指令
同时 Avatar也具有AI 并设置 controlby = NONE 即，行动也由服务器端控制



role/cardID  and level skillConfig  equipConfig to init every character's attr


}




战斗大厅：（和好友一起加入   ；  搜索加入）
{
 room：
	多个实体加入同一副本  
}




副本逻辑实现






spaceManager config
{

	character spawn pos{

	}

	rules{
		Player Target  :K boss；守护xx 多久或者多少波怪；死斗无时间限制直到全部死亡；
		event atTime
		start;bossTime;timeLimted;Fail&destroy
	}

	monsters{
		{role  level num spawnAtTime}

		Monstar Target

	}

	boss{
		;bossCrazyTime   equip  skill精魄 技能书/技能信息球（信息扰动）
	}


	{rewards }


}

副本销毁问题

副本逻辑结束 将玩家踢出空间 并销毁自己
玩家断线 副本中检测到无任何玩家则过一段时间后 副本自动销毁
玩家离开副本 副本中检测到无任何玩家则副本自动销毁




account 
{
ownCharacters:[
	{character1 :role/cardID,data[level,],skillConfig,equipConfig}
	{character2 :role/cardID,data[level],skillConfig,equipConfig}
	{character5 :role/cardID,data[level],skillConfig,equipConfig}
	{character6 :role/cardID,data[level],skillConfig,equipConfig}
	{character8 :role/cardID,data[level],skillConfig,equipConfig}
]

bag:[
{	
	skillcard
	equipment
	}
]


}



对于副本来说 因为大量的相同副本的地图信息是一样的 是否有更好的解决方法来统一使用相同地图的导航 以节省消耗;或者说可以怎么设计逻辑？




KBEngine.entities.get(xxx).__dict__
KBEngine.entities.get(1030).jump
KBEngine.entities.keys()


#字典遍历
	for key, data in dictData.items()

	for key in dictData:

	for k in dictData.iterkeys():

	for k,v in zip(dictData.iterkeys(), dictData.itervalues()):


列表遍历
	for app_id in app_list:
	for index,app_id in enumerate(app_list):
	for i in range(len(app_list)):
	for app_id in iter(app_list):