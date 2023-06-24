# -*- coding: utf-8 -*-
import KBEngine
import GlobalConst
import d_spaces
import d_avatar_inittab
import GlobalDefine
from KBEDebug import * 

class Teleport:
	def __init__(self):

		pass

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onClientEnabled(self):
		"""
		为Avatar所调用，登录到空间。
		默认登录，跳到home。但是否可能会断线重连需要回到之前的space。
		#TODO：测试celldata被创建时候 是否是从之前断线时保存的加载的
		"""
		if self.cell is not None:
			return 

		# 防止使用同一个号登陆不同的demo造成无法找到匹配的地图从而无法加载资源导致无法进入游戏
		# 这里检查一下， 发现不对则强制同步到匹配的地图
		# 忽略机器人的检查
		# if hasattr(self, "cellData") and self.getClientType() != 6:
		# 	# 如果角色跳转到了同属某个demo的其他场景那么不强制回到出生的主场景
		# 	if self.cellData["spaceUType"] in GlobalConst.g_demoMaps.values():
		# 		spaceUType = GlobalConst.g_demoMaps.get(self.getClientDatas()[0], 1)

		# 		if self.cellData["spaceUType"] != spaceUType:
		# 			spacedatas = d_spaces.datas[spaceUType]
		# 			self.spaceUTypeB = spaceUType
		# 			self.cellData["spaceUType"] = spaceUType
		# 			self.cellData["position"] = spacedatas.get("spawnPos", (0,0,0))
		

		DEBUG_MSG("teleport onClientEnabled::%s." % (self.__dict__))

		#old space not found, teleport to self home space
		if not KBEngine.globalData["SpaceMgr"].isSpaceExist(self.spaceUTypeB,self.cellData["spacekey"]):
			DEBUG_MSG("teleport onClientEnabled:: old space not found, teleport to self home space" )
			self.spaceUTypeB = GlobalDefine.HOMESPACE_UTYPE
			self.cellData["spaceKey"] = self.accountEntity.homeSpaceKey
			DEBUG_MSG("teleport onClientEnabled:: self.cellData[spaceKey] %s." % (self.cellData["spaceKey"]))
			#由于没有找到之前的space，则需要会到homespace。
			spacedatas = d_spaces.datas[self.spaceUTypeB]
			self.cellData["position"] = spacedatas["spawnPos"]
			self.cellData["direction"] = (0, 0, spacedatas["spawnYaw"])
		else:
			DEBUG_MSG("teleport onClientEnabled:: find space from db. return to spacespaceUTypeB:%s[spaceKey] %s." % (self.spaceUTypeB,self.cellData["spaceKey"]))


		#KBEngine.globalData["Spaces"].loginToSpace(self, self.spaceUTypeB, SpaceContext.createContext(self, self.spaceUTypeB))
		KBEngine.globalData["SpaceMgr"].loginToSpace(self, self.spaceUTypeB, {"spaceKey":self.cellData["spacekey"]})


