# Embedded file name: scripts/common/Lib/plat-mac/Carbon/Files.py


def FOUR_CHAR_CODE(x):
    return x


true = True
false = False
fsCurPerm = 0
fsRdPerm = 1
fsWrPerm = 2
fsRdWrPerm = 3
fsRdWrShPerm = 4
fsRdDenyPerm = 16
fsWrDenyPerm = 32
fsRtParID = 1
fsRtDirID = 2
fsAtMark = 0
fsFromStart = 1
fsFromLEOF = 2
fsFromMark = 3
pleaseCacheBit = 4
pleaseCacheMask = 16
noCacheBit = 5
noCacheMask = 32
rdVerifyBit = 6
rdVerifyMask = 64
rdVerify = 64
forceReadBit = 6
forceReadMask = 64
newLineBit = 7
newLineMask = 128
newLineCharMask = 65280
fsSBPartialName = 1
fsSBFullName = 2
fsSBFlAttrib = 4
fsSBFlFndrInfo = 8
fsSBFlLgLen = 32
fsSBFlPyLen = 64
fsSBFlRLgLen = 128
fsSBFlRPyLen = 256
fsSBFlCrDat = 512
fsSBFlMdDat = 1024
fsSBFlBkDat = 2048
fsSBFlXFndrInfo = 4096
fsSBFlParID = 8192
fsSBNegate = 16384
fsSBDrUsrWds = 8
fsSBDrNmFls = 16
fsSBDrCrDat = 512
fsSBDrMdDat = 1024
fsSBDrBkDat = 2048
fsSBDrFndrInfo = 4096
fsSBDrParID = 8192
fsSBPartialNameBit = 0
fsSBFullNameBit = 1
fsSBFlAttribBit = 2
fsSBFlFndrInfoBit = 3
fsSBFlLgLenBit = 5
fsSBFlPyLenBit = 6
fsSBFlRLgLenBit = 7
fsSBFlRPyLenBit = 8
fsSBFlCrDatBit = 9
fsSBFlMdDatBit = 10
fsSBFlBkDatBit = 11
fsSBFlXFndrInfoBit = 12
fsSBFlParIDBit = 13
fsSBNegateBit = 14
fsSBDrUsrWdsBit = 3
fsSBDrNmFlsBit = 4
fsSBDrCrDatBit = 9
fsSBDrMdDatBit = 10
fsSBDrBkDatBit = 11
fsSBDrFndrInfoBit = 12
fsSBDrParIDBit = 13
bLimitFCBs = 31
bLocalWList = 30
bNoMiniFndr = 29
bNoVNEdit = 28
bNoLclSync = 27
bTrshOffLine = 26
bNoSwitchTo = 25
bDontShareIt = 21
bNoDeskItems = 20
bNoBootBlks = 19
bAccessCntl = 18
bNoSysDir = 17
bHasExtFSVol = 16
bHasOpenDeny = 15
bHasCopyFile = 14
bHasMoveRename = 13
bHasDesktopMgr = 12
bHasShortName = 11
bHasFolderLock = 10
bHasPersonalAccessPrivileges = 9
bHasUserGroupList = 8
bHasCatSearch = 7
bHasFileIDs = 6
bHasBTreeMgr = 5
bHasBlankAccessPrivileges = 4
bSupportsAsyncRequests = 3
bSupportsTrashVolumeCache = 2
bIsEjectable = 0
bSupportsHFSPlusAPIs = 1
bSupportsFSCatalogSearch = 2
bSupportsFSExchangeObjects = 3
bSupports2TBFiles = 4
bSupportsLongNames = 5
bSupportsMultiScriptNames = 6
bSupportsNamedForks = 7
bSupportsSubtreeIterators = 8
bL2PCanMapFileBlocks = 9
bParentModDateChanges = 10
bAncestorModDateChanges = 11
bSupportsSymbolicLinks = 13
bIsAutoMounted = 14
bAllowCDiDataHandler = 17
kLargeIcon = 1
kLarge4BitIcon = 2
kLarge8BitIcon = 3
kSmallIcon = 4
kSmall4BitIcon = 5
kSmall8BitIcon = 6
kicnsIconFamily = 239
kLargeIconSize = 256
kLarge4BitIconSize = 512
kLarge8BitIconSize = 1024
kSmallIconSize = 64
kSmall4BitIconSize = 128
kSmall8BitIconSize = 256
kWidePosOffsetBit = 8
kUseWidePositioning = 1 << kWidePosOffsetBit
kMaximumBlocksIn4GB = 8388607
fsUnixPriv = 1
kNoUserAuthentication = 1
kPassword = 2
kEncryptPassword = 3
kTwoWayEncryptPassword = 6
kOwnerID2Name = 1
kGroupID2Name = 2
kOwnerName2ID = 3
kGroupName2ID = 4
kReturnNextUser = 1
kReturnNextGroup = 2
kReturnNextUG = 3
kVCBFlagsIdleFlushBit = 3
kVCBFlagsIdleFlushMask = 8
kVCBFlagsHFSPlusAPIsBit = 4
kVCBFlagsHFSPlusAPIsMask = 16
kVCBFlagsHardwareGoneBit = 5
kVCBFlagsHardwareGoneMask = 32
kVCBFlagsVolumeDirtyBit = 15
kVCBFlagsVolumeDirtyMask = 32768
kioVAtrbDefaultVolumeBit = 5
kioVAtrbDefaultVolumeMask = 32
kioVAtrbFilesOpenBit = 6
kioVAtrbFilesOpenMask = 64
kioVAtrbHardwareLockedBit = 7
kioVAtrbHardwareLockedMask = 128
kioVAtrbSoftwareLockedBit = 15
kioVAtrbSoftwareLockedMask = 32768
kioFlAttribLockedBit = 0
kioFlAttribLockedMask = 1
kioFlAttribResOpenBit = 2
kioFlAttribResOpenMask = 4
kioFlAttribDataOpenBit = 3
kioFlAttribDataOpenMask = 8
kioFlAttribDirBit = 4
kioFlAttribDirMask = 16
ioDirFlg = 4
ioDirMask = 16
kioFlAttribCopyProtBit = 6
kioFlAttribCopyProtMask = 64
kioFlAttribFileOpenBit = 7
kioFlAttribFileOpenMask = 128
kioFlAttribInSharedBit = 2
kioFlAttribInSharedMask = 4
kioFlAttribMountedBit = 3
kioFlAttribMountedMask = 8
kioFlAttribSharePointBit = 5
kioFlAttribSharePointMask = 32
kioFCBWriteBit = 8
kioFCBWriteMask = 256
kioFCBResourceBit = 9
kioFCBResourceMask = 512
kioFCBWriteLockedBit = 10
kioFCBWriteLockedMask = 1024
kioFCBLargeFileBit = 11
kioFCBLargeFileMask = 2048
kioFCBSharedWriteBit = 12
kioFCBSharedWriteMask = 4096
kioFCBFileLockedBit = 13
kioFCBFileLockedMask = 8192
kioFCBOwnClumpBit = 14
kioFCBOwnClumpMask = 16384
kioFCBModifiedBit = 15
kioFCBModifiedMask = 32768
kioACUserNoSeeFolderBit = 0
kioACUserNoSeeFolderMask = 1
kioACUserNoSeeFilesBit = 1
kioACUserNoSeeFilesMask = 2
kioACUserNoMakeChangesBit = 2
kioACUserNoMakeChangesMask = 4
kioACUserNotOwnerBit = 7
kioACUserNotOwnerMask = 128
kioACAccessOwnerBit = 31
kioACAccessBlankAccessBit = 28
kioACAccessBlankAccessMask = 268435456
kioACAccessUserWriteBit = 26
kioACAccessUserWriteMask = 67108864
kioACAccessUserReadBit = 25
kioACAccessUserReadMask = 33554432
kioACAccessUserSearchBit = 24
kioACAccessUserSearchMask = 16777216
kioACAccessEveryoneWriteBit = 18
kioACAccessEveryoneWriteMask = 262144
kioACAccessEveryoneReadBit = 17
kioACAccessEveryoneReadMask = 131072
kioACAccessEveryoneSearchBit = 16
kioACAccessEveryoneSearchMask = 65536
kioACAccessGroupWriteBit = 10
kioACAccessGroupWriteMask = 1024
kioACAccessGroupReadBit = 9
kioACAccessGroupReadMask = 512
kioACAccessGroupSearchBit = 8
kioACAccessGroupSearchMask = 256
kioACAccessOwnerWriteBit = 2
kioACAccessOwnerWriteMask = 4
kioACAccessOwnerReadBit = 1
kioACAccessOwnerReadMask = 2
kioACAccessOwnerSearchBit = 0
kioACAccessOwnerSearchMask = 1
kfullPrivileges = 458759
kownerPrivileges = 7
knoUser = 0
kadministratorUser = 1
knoGroup = 0
AppleShareMediaType = FOUR_CHAR_CODE('afpm')
volMountNoLoginMsgFlagBit = 0
volMountNoLoginMsgFlagMask = 1
volMountExtendedFlagsBit = 7
volMountExtendedFlagsMask = 128
volMountInteractBit = 15
volMountInteractMask = 32768
volMountChangedBit = 14
volMountChangedMask = 16384
volMountFSReservedMask = 255
volMountSysReservedMask = 65280
kAFPExtendedFlagsAlternateAddressMask = 1
kAFPTagTypeIP = 1
kAFPTagTypeIPPort = 2
kAFPTagTypeDDP = 3
kAFPTagTypeDNS = 4
kAFPTagLengthIP = 6
kAFPTagLengthIPPort = 8
kAFPTagLengthDDP = 6
kFSInvalidVolumeRefNum = 0
kFSCatInfoNone = 0
kFSCatInfoTextEncoding = 1
kFSCatInfoNodeFlags = 2
kFSCatInfoVolume = 4
kFSCatInfoParentDirID = 8
kFSCatInfoNodeID = 16
kFSCatInfoCreateDate = 32
kFSCatInfoContentMod = 64
kFSCatInfoAttrMod = 128
kFSCatInfoAccessDate = 256
kFSCatInfoBackupDate = 512
kFSCatInfoPermissions = 1024
kFSCatInfoFinderInfo = 2048
kFSCatInfoFinderXInfo = 4096
kFSCatInfoValence = 8192
kFSCatInfoDataSizes = 16384
kFSCatInfoRsrcSizes = 32768
kFSCatInfoSharingFlags = 65536
kFSCatInfoUserPrivs = 131072
kFSCatInfoUserAccess = 524288
kFSCatInfoAllDates = 992
kFSCatInfoGettableInfo = 262143
kFSCatInfoSettableInfo = 8163
kFSNodeLockedBit = 0
kFSNodeLockedMask = 1
kFSNodeResOpenBit = 2
kFSNodeResOpenMask = 4
kFSNodeDataOpenBit = 3
kFSNodeDataOpenMask = 8
kFSNodeIsDirectoryBit = 4
kFSNodeIsDirectoryMask = 16
kFSNodeCopyProtectBit = 6
kFSNodeCopyProtectMask = 64
kFSNodeForkOpenBit = 7
kFSNodeForkOpenMask = 128
kFSNodeInSharedBit = 2
kFSNodeInSharedMask = 4
kFSNodeIsMountedBit = 3
kFSNodeIsMountedMask = 8
kFSNodeIsSharePointBit = 5
kFSNodeIsSharePointMask = 32
kFSIterateFlat = 0
kFSIterateSubtree = 1
kFSIterateDelete = 2
fsSBNodeID = 32768
fsSBAttributeModDate = 65536
fsSBAccessDate = 131072
fsSBPermissions = 262144
fsSBNodeIDBit = 15
fsSBAttributeModDateBit = 16
fsSBAccessDateBit = 17
fsSBPermissionsBit = 18
kFSAllocDefaultFlags = 0
kFSAllocAllOrNothingMask = 1
kFSAllocContiguousMask = 2
kFSAllocNoRoundUpMask = 4
kFSAllocReservedMask = 65528
kFSVolInfoNone = 0
kFSVolInfoCreateDate = 1
kFSVolInfoModDate = 2
kFSVolInfoBackupDate = 4
kFSVolInfoCheckedDate = 8
kFSVolInfoFileCount = 16
kFSVolInfoDirCount = 32
kFSVolInfoSizes = 64
kFSVolInfoBlocks = 128
kFSVolInfoNextAlloc = 256
kFSVolInfoRsrcClump = 512
kFSVolInfoDataClump = 1024
kFSVolInfoNextID = 2048
kFSVolInfoFinderInfo = 4096
kFSVolInfoFlags = 8192
kFSVolInfoFSInfo = 16384
kFSVolInfoDriveInfo = 32768
kFSVolInfoGettableInfo = 65535
kFSVolInfoSettableInfo = 12292
kFSVolFlagDefaultVolumeBit = 5
kFSVolFlagDefaultVolumeMask = 32
kFSVolFlagFilesOpenBit = 6
kFSVolFlagFilesOpenMask = 64
kFSVolFlagHardwareLockedBit = 7
kFSVolFlagHardwareLockedMask = 128
kFSVolFlagSoftwareLockedBit = 15
kFSVolFlagSoftwareLockedMask = 32768
kFNDirectoryModifiedMessage = 1
kFNNoImplicitAllSubscription = 1
rAliasType = FOUR_CHAR_CODE('alis')
kARMMountVol = 1
kARMNoUI = 2
kARMMultVols = 8
kARMSearch = 256
kARMSearchMore = 512
kARMSearchRelFirst = 1024
asiZoneName = -3
asiServerName = -2
asiVolumeName = -1
asiAliasName = 0
asiParentName = 1
kResolveAliasFileNoUI = 1
kClippingCreator = FOUR_CHAR_CODE('drag')
kClippingPictureType = FOUR_CHAR_CODE('clpp')
kClippingTextType = FOUR_CHAR_CODE('clpt')
kClippingSoundType = FOUR_CHAR_CODE('clps')
kClippingUnknownType = FOUR_CHAR_CODE('clpu')
kInternetLocationCreator = FOUR_CHAR_CODE('drag')
kInternetLocationHTTP = FOUR_CHAR_CODE('ilht')
kInternetLocationFTP = FOUR_CHAR_CODE('ilft')
kInternetLocationFile = FOUR_CHAR_CODE('ilfi')
kInternetLocationMail = FOUR_CHAR_CODE('ilma')
kInternetLocationNNTP = FOUR_CHAR_CODE('ilnw')
kInternetLocationAFP = FOUR_CHAR_CODE('ilaf')
kInternetLocationAppleTalk = FOUR_CHAR_CODE('ilat')
kInternetLocationNSL = FOUR_CHAR_CODE('ilns')
kInternetLocationGeneric = FOUR_CHAR_CODE('ilge')
kCustomIconResource = -16455
kCustomBadgeResourceType = FOUR_CHAR_CODE('badg')
kCustomBadgeResourceID = kCustomIconResource
kCustomBadgeResourceVersion = 0
kRoutingResourceType = FOUR_CHAR_CODE('rout')
kRoutingResourceID = 0
kContainerFolderAliasType = FOUR_CHAR_CODE('fdrp')
kContainerTrashAliasType = FOUR_CHAR_CODE('trsh')
kContainerHardDiskAliasType = FOUR_CHAR_CODE('hdsk')
kContainerFloppyAliasType = FOUR_CHAR_CODE('flpy')
kContainerServerAliasType = FOUR_CHAR_CODE('srvr')
kApplicationAliasType = FOUR_CHAR_CODE('adrp')
kContainerAliasType = FOUR_CHAR_CODE('drop')
kDesktopPrinterAliasType = FOUR_CHAR_CODE('dtpa')
kContainerCDROMAliasType = FOUR_CHAR_CODE('cddr')
kApplicationCPAliasType = FOUR_CHAR_CODE('acdp')
kApplicationDAAliasType = FOUR_CHAR_CODE('addp')
kPackageAliasType = FOUR_CHAR_CODE('fpka')
kAppPackageAliasType = FOUR_CHAR_CODE('fapa')
kSystemFolderAliasType = FOUR_CHAR_CODE('fasy')
kAppleMenuFolderAliasType = FOUR_CHAR_CODE('faam')
kStartupFolderAliasType = FOUR_CHAR_CODE('fast')
kPrintMonitorDocsFolderAliasType = FOUR_CHAR_CODE('fapn')
kPreferencesFolderAliasType = FOUR_CHAR_CODE('fapf')
kControlPanelFolderAliasType = FOUR_CHAR_CODE('fact')
kExtensionFolderAliasType = FOUR_CHAR_CODE('faex')
kExportedFolderAliasType = FOUR_CHAR_CODE('faet')
kDropFolderAliasType = FOUR_CHAR_CODE('fadr')
kSharedFolderAliasType = FOUR_CHAR_CODE('fash')
kMountedFolderAliasType = FOUR_CHAR_CODE('famn')
kIsOnDesk = 1
kColor = 14
kIsShared = 64
kHasNoINITs = 128
kHasBeenInited = 256
kHasCustomIcon = 1024
kIsStationery = 2048
kNameLocked = 4096
kHasBundle = 8192
kIsInvisible = 16384
kIsAlias = 32768
fOnDesk = kIsOnDesk
fHasBundle = kHasBundle
fInvisible = kIsInvisible
fTrash = -3
fDesktop = -2
fDisk = 0
kIsStationary = kIsStationery
kExtendedFlagsAreInvalid = 32768
kExtendedFlagHasCustomBadge = 256
kExtendedFlagHasRoutingInfo = 4
kFirstMagicBusyFiletype = FOUR_CHAR_CODE('bzy ')
kLastMagicBusyFiletype = FOUR_CHAR_CODE('bzy?')
kMagicBusyCreationDate = 1329266096