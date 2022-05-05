COMMUN_TEST_CASE = [
        "saiacl.IPAclTest",
        "saiacl.MACSrcAclTest",
        "saiacl.L3AclTest",
        "saiacl.SeqAclTableGroupTest",
        "saiacl.MultBindAclTableGroupTest",
        "saiacl.BindAclTableInGroupTest",
        "saiacl.L3AclTableTestI",
        "saiacl.L3AclTableGroupTestI",
        "saiacl.L3AclTableGroupTestII",
        "saiacl.L3AclTableTestII",
        "saidebugcounters.DropMCSMAC",
        "saidebugcounters.DropSMACequalsDMAC",
        "saidebugcounters.DropDMACReserved",
        "saidebugcounters.DropIngressVLANFilter",
        "saidebugcounters.DropL2LoopbackFilter",
        "saidebugcounters.DropL3LoopbackFilter",
        "saidebugcounters.DropNonRoutable",
        "saidebugcounters.DropNoL3Header",
        "saidebugcounters.DropIPHeaderError",
        "saidebugcounters.DropUCDIPMCDMAC",
        "saidebugcounters.DropDIPLoopback",
        "saidebugcounters.DropSIPLoopback",
        "saidebugcounters.DropMulticastSIP",
        "saidebugcounters.DropSIPClassE",
        "saidebugcounters.DropSIPUnspecified",
        "saidebugcounters.DropMCDMACMismatch",
        "saidebugcounters.DropSIPEqualsDIP",
        "saidebugcounters.DropSIPBC",
        "saidebugcounters.DropDIPLocal",
        "saidebugcounters.DropDIPLinkLocal",
        "saidebugcounters.DropSIPLinkLocal",
        "saidebugcounters.DropIPv6MCScope0",
        "saidebugcounters.DropIPv6MCScope1",
        "saidebugcounters.DropIRIFDisabled",
        "saidebugcounters.DropERIFDisabled",
        "saidebugcounters.DropLPM4Miss",
        "saidebugcounters.DropLPM6Miss",
        "saidebugcounters.DropBlackholeRoute",
        "saidebugcounters.DropACLAny",
        "saidebugcounters.NoDropIngressVLANFilter",
        "saidebugcounters.DropMultipleReasons",
        "saidebugcounters.EditingDropReasons",
        "saifdb.L2FDBMissUnicastTest",
        "saifdb.L2FDBMissBroadcastTest",
        "saihostif.NoPolicyTest",
        "saihostif.PolicyTest",
        "saihostif.ARPTest",
        "saihostif.DHCPTest",
        "saihostif.LLDPTest",
        "saihostif.LACPTest",
        "saihostif.SNMPTest",
        "saihostif.SSHTest",
        "saihostif.IP2METest",
        "saihostif.TTLErrorTest",
        "saihostif.BGPTest",
        "sail2.L2AccessToAccessVlanTest",
        "sail2.L2TrunkToTrunkVlanTest",
        "sail2.L2AccessToTrunkVlanTest",
        "sail2.L2TrunkToAccessVlanTest",
        "sail2.L2FloodTest",
        "sail2.L2LagTest",
        "sail2.LagHashseedTest",
        "sail2.L2VlanBcastUcastTest",
        "sail2.L2FdbAgingTest",
        "sail2.L2ARPRequestReplyFDBLearningTest",
        "sail2.L2BridgeSubPortFloodTest",
        "sail2.L2BridgePortTestI",
        "sail2.L2BridgeSubPortFDBTest",
        "sail2.L2MtuTest",
        "sail2.L2MacMoveTestI ",
        "sail2.L2MacMoveTestII ",
        "sail2.L2MacMoveTestIII ",
        "sail3.L3IPv4HostTest",
        "sail3.L3IPv4LpmTest",
        "sail3.L3IPv6HostTest",
        "sail3.L3IPv6PrefixTest",
        "sail3.L3IPv6LpmTest",
        "sail3.L3IPv4EcmpHostTest",
        "sail3.L3IPv6EcmpHostTest",
        "sail3.L3IPv4EcmpLpmTest",
        "sail3.L3IPv6EcmpLpmTest",
        "sail3.L3IPv4EcmpHashSeedTest",
        "sail3.L3IPv4LagTest",
        "sail3.L3IPv6LagTest",
        "sail3.L3EcmpLagTest",
        "sail3.L3EcmpLagTestMini",
        "sail3.L3VIIPv4HostTest",
        "sail3.L3IPv4MacRewriteTest",
        "sail3.L3VlanNeighborMacUpdateTest",
        "sail3.L3MultipleLagTest",
        "sail3.L3MultipleEcmpLagTest",
        "sail3.L3BridgeAndSubPortRifTest",
        "sail3.L3SubPortAndVLANRifTest",
        "sail3.L3MtuTest",
        "sail3.L3IPv4NeighborMacTest",
        "sail3.L3IPv6NeighborMacTest",
        "sail3.L3IPv4NeighborFdbAgeoutTest",
        "sail3.L3IPv6NeighborFdbAgeoutTest",
        "sail3.L3IPv4EcmpGroupMemberTest",
        "sail3.L3IPv6EcmpGroupMemberTest",
        "sail3.L3IPv4_32Test ",
        "sail3.L3LpbkSubnetTest",
        "saimirror.IngressLocalMirrorTest",
        "saimirror.IngressRSpanMirrorTest",
        "saimirror.IngressERSpanMirrorTest",
        "saimirror.EgressLocalMirrorTest",
        "saimirror.EgressERSpanMirrorTest",
        "saitunnel.IpIpEncapTest",
        "saitunnel.IpIpP2PTunnelDecapTest",
        "saitunnel.IpIpP2PTunnelDecapOnlyTestBase",
        "saitunnel.IpIpP2PTunnelDecapTestIpv4inIpv4",
        "saitunnel.IpIpP2PTunnelDecapTestIpv6inIpv4",
        "saitunnel.IpIpP2PTunnelDecapTestIpv4inIpv6",
        "saitunnel.IpIpP2PTunnelDecapTestIpv6inIpv6",
        "saitunnel.IpIpP2PTunnelDecapTestIpv4inIpv4GRE",
        "saitunnel.IpIpP2PTunnelDecapTestIpv6inIpv4GRE",
        "saitunnel.IpIpP2PTunnelDecapTestIpv4inIpv6GRE",
        "saitunnel.IpIpP2PTunnelDecapTestIpv6inIpv6GRE"
        ]


PTF_SAI_TEST_CASE = [
        "saisanity.L2TrunkToTrunkVlanTest",
        "saisanity.L2TrunkToAccessVlanTest",
        "saisanity.L2SanityTest"
        ]

WARM_BOOT_TEST_CASE = [
        "warm_saisanity.WarmL2SanityTest"
        ]


PROBE_TEST_CASE = "sail3.L3IPv4HostTest"
