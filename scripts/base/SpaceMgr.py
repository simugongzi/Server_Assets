# -*- coding: utf-8 -*-
import KBEngine
import Functor
import d_spaces
import SCDefine
import Watcher
from KBEDebug import *
from SpaceAlloc import *
from interfaces.GameObject import GameObject

class SpaceMgr(KBEngine.Entity, GameObject):

	"""
	这是一个脚本层封装的空间管理器
	KBEngine的space是一个抽象空间的概念，一个空间可以被脚本层视为游戏场景、游戏房间、甚至是一个宇宙。
	"""
	def __init__(self):
		KBEngine.Entity.__init__(self)
		GameObject.__init__(self)
		
		# 服务器开启，就创建所有的大世界space
		self.initDefaultMapAlloc()
		
		# 向全局共享数据中注册这个管理器的entityCall以便在所有逻辑进程中可以方便的访问
		KBEngine.globalData["SpaceMgr"] = self

	#TODO：这里改为创建大厅或者世界频道、和商城
	def initDefaultMapAlloc(self):
		# 注册一个定时器，在这个定时器中我们每个周期都创建出一些大世界，直到创建完所有
		self._spaceAllocs = {}
		self.addTimer(3, 1, SCDefine.TIMER_TYPE_CREATE_SPACES)
		#目前大世界地图就一个ST_HALL大厅，后续看是否要做大世界地图
		self._tmpDatas = list(d_spaces.datas.keys())
		for utype in self._tmpDatas:
			spaceData = d_spaces.datas.get(utype)
			if spaceData["entityType"] == "SpaceDuplicate":
				self._spaceAllocs[utype] = SpaceAllocDuplicate(utype)
			else:
				self._spaceAllocs[utype] = SpaceAlloc(utype)
	
	
	def getSpaceAllocs(self):
		return self._spaceAllocs
		
	def createWorldSpaceOnTimer(self, tid):
		"""
		创建space
		"""
		if len(self._tmpDatas) > 0:
			spaceUType = self._tmpDatas.pop(0)
			self._spaceAllocs[spaceUType].init({})
			
		if len(self._tmpDatas) <= 0:
			del self._tmpDatas
			self.delTimer(tid)
			
	def loginToSpace(self, avatarEntity, spaceUType, context):
		"""
		defined method.
		某个玩家请求登陆到某个space中
		"""
		self._spaceAllocs[spaceUType].loginToSpace(avatarEntity, context)
	
	def logoutSpace(self, avatarID, spaceKey):
		"""
		defined method.
		某个玩家请求登出这个space
		好像暂时没有调用者
		"""
		#TODO 请求登出，应该携带当前space的spaceutype
		for spaceAlloc in self._spaceAllocs.values():
			space = spaceAlloc.getSpaces().get(spaceKey)
			if space:
				space.logoutSpace(avatarID)
				
	def teleportSpace(self, entityCall, spaceUType, position, direction, context):
		"""
		defined method.
		请求进入某个space中
		"""
		self._spaceAllocs[spaceUType].teleportSpace(entityCall, position, direction, context)



	def creatDynamicsSpace(self,spaceUType,spaceKey):
		"""
		按需实时创建副本space
		"""

		if self._spaceAllocs[spaceUType] == None:
			spaceData = d_spaces.datas.get(spaceUType)
			if spaceData["entityType"] == "SpaceDuplicate":
				self._spaceAllocs[spaceUType] = SpaceAllocDuplicate(spaceUType)
			else:
				self._spaceAllocs[spaceUType] = SpaceAlloc(spaceUType)
		else:
			DEBUG_MSG("creatSpace _spaceAllocs[spaceUType]  exist" )

		if spaceKey != None and spaceKey != 0:
			self._spaceAllocs[spaceUType].init({"spaceKey" : spaceKey})
		else:
			self._spaceAllocs[spaceUType].init({})


	
	def isSpaceExist(self,spaceUType,spaceKey):
		"""
		根据spaceUType和spaceKey查看space是否存在
		"""
		if spaceUType in self._spaceAllocs.keys():
			if spaceKey in self._spaceAllocs[spaceUType].getSpaces().keys():
				return True
		return False
		


	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		#DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
		if SCDefine.TIMER_TYPE_CREATE_SPACES == userArg:
			self.createWorldSpaceOnTimer(tid)
		
		GameObject.onTimer(self, tid, userArg)
		
	def onSpaceLoseCell(self, spaceUType, spaceKey):
		"""
		defined method.
		space的cell创建好了
		"""
		self._spaceAllocs[spaceUType].onSpaceLoseCell(spaceKey)
		
	def onSpaceGetCell(self, spaceUType, spaceEntityCall, spaceKey):
		"""
		defined method.
		space的cell创建好了
		"""
		self._spaceAllocs[spaceUType].onSpaceGetCell(spaceEntityCall, spaceKey)

