
https://app.diagrams.net/#Hsimugongzi%2FServerDoc%2Fmain%2FServer.drawio



pip install kbengine_tips


try:
    import KBEngine
except ImportError:
    from kbengine_tips.BaseApp import KBEngine



DEBUG_MSG('simu  xx (%s) ' % (   ))
WARNING_MSG("SIMU test  ")
TRACE_MSG("SIMU test  ")
INFO_MSG("SIMU test  ")
WARNING_MSG("SIMU test  ")
ERROR_MSG("SIMU test  ")

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
		;bossCrazyTime   equip  skill精魄
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