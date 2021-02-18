#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 17:23
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : test_compute_navigation.py
# @Software: PyCharm

import allure
import pytest
from page_action.select_product_and_service_action import Select_Produce_And_Service_Action
from page_action.feature_action import Feature_Action
from util.tools import p
from util.logger import logger

@allure.feature("导航功能测试")
@pytest.mark.navigation
@pytest.mark.usefixtures("driver")
class Test_Compute_Navigation():

    @pytest.mark.run(order=1)
    def test_navigation_to_instance(self,driver):
        """测试导航到主机页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_instance()
        fa = Feature_Action(driver)
        fa.skip()  #第一次进入计算服务时会弹出引导弹框，这里用于跳过引导
        obj.sleep(2)
        assert "/instances/" in obj.get_url()

    @pytest.mark.run(order=2)
    def test_navigation_to_instance_reserved_contracts(self,driver):
        """测试导航到主机_预留合约页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_instance_reserved_contracts()
        obj.sleep(2)
        assert "/instances/reserved_contracts/" in obj.get_url()

    @pytest.mark.run(order=3)
    def test_navigation_to_instance_instance_groups(self, driver):
        """测试导航到主机_安置策略组页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_instance_instance_groups()
        obj.sleep(2)
        assert "/instances/instance_groups/" in obj.get_url()

    @pytest.mark.run(order=4)
    def test_navigation_to_image(self,driver):
        """测试导航到映像页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_images()
        obj.sleep(2)
        assert "/images/" in obj.get_url()

    @pytest.mark.run(order=5)
    def test_navigation_to_image_self(self, driver):
        """测试导航到映像_自有页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_image_self()
        obj.sleep(2)
        assert "/images/self/" in obj.get_url()

    @pytest.mark.run(order=6)
    def test_navigation_to_image_shared(self, driver):
        """测试导航到映像_共享页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_image_shared()
        obj.sleep(2)
        assert "/images/shared/" in obj.get_url()

    @pytest.mark.run(order=7)
    def test_navigation_to_image_market(self, driver):
        """测试导航到映像_市场页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_image_market()
        obj.sleep(2)
        assert "/images/market/" in obj.get_url()

    @pytest.mark.run(order=8)
    def test_navigation_to_keypairs(self, driver):
        """测试导航到SSH密钥页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_keypairs()
        obj.sleep(2)
        assert "/keypairs/" in obj.get_url()

    @pytest.mark.run(order=9)
    def test_navigation_to_devices(self, driver):
        """测试导航到设备页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_devices()
        obj.sleep(2)
        assert "/devices/" in obj.get_url()

    @pytest.mark.run(order=10)
    def test_navigation_to_nics(self, driver):
        """测试导航到网卡页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_nics()
        obj.sleep(2)
        assert "/nics/" in obj.get_url()

    @pytest.mark.run(order=11)
    def test_navigation_to_routers(self, driver):
        """测试导航到VPC是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_routers()
        obj.sleep(2)
        assert "/routers/" in obj.get_url()

    @pytest.mark.run(order=12)
    def test_navigation_to_loadbalancers(self, driver):
        """测试导航到负载均衡器_负载均衡器页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_loadbalancers()
        obj.sleep(2)
        assert "/loadbalancers/" in obj.get_url()

    @pytest.mark.run(order=13)
    def test_navigation_to_loadbalancers_loadbalancer_policies(self, driver):
        """测试导航到负载均衡器_转发策略页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_loadbalancers_loadbalancer_policies()
        obj.sleep(2)
        assert "/loadbalancers/loadbalancer_policies/" in obj.get_url()

    @pytest.mark.run(order=14)
    def test_navigation_to_loadbalancers_server_certificates(self, driver):
        """测试导航到负载均衡器_服务器证书页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_loadbalancers_server_certificates()
        obj.sleep(2)
        assert "/loadbalancers/server_certificates/" in obj.get_url()

    @pytest.mark.run(order=15)
    def test_navigation_to_vxnets(self, driver):
        """测试导航到私有网络页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_vxnets()
        obj.sleep(2)
        assert "/vxnets/" in obj.get_url()

    @pytest.mark.run(order=16)
    def test_navigation_to_routing_tables(self, driver):
        """测试导航到路由表页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_routing_tables()
        obj.sleep(2)
        assert "/routing_tables/" in obj.get_url()

    @pytest.mark.run(order=17)
    def test_navigation_to_eips(self, driver):
        """测试导航到公网 IP页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_eips()
        obj.sleep(2)
        assert "/eips/" in obj.get_url()

    @pytest.mark.run(order=18)
    def test_navigation_to_eips_eip_v6(self, driver):
        """测试导航到公网 IP页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_eip_v6()
        obj.sleep(2)
        assert "/eips/eip_v6/" in obj.get_url()

    @pytest.mark.run(order=19)
    def test_navigation_to_nfvs(self, driver):
        """测试导航到NAT 网关页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_nfvs()
        obj.sleep(2)
        assert "/nfvs/" in obj.get_url()

    @pytest.mark.run(order=20)
    def test_navigation_to_dns_aliases(self, driver):
        """测试导航到内网域名别名页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_dns_aliases()
        obj.sleep(2)
        assert "/dns_aliases/" in obj.get_url()

    @pytest.mark.run(order=21)
    def test_navigation_to_dns_aliases(self, driver):
        """测试导航到边界路由器页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_intranet_routers()
        obj.sleep(2)
        assert "/intranet_routers/" in obj.get_url()

    @pytest.mark.run(order=22)
    def test_navigation_to_dns_aliases(self, driver):
        """测试导航到网络流量镜像页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_spans()
        obj.sleep(2)
        assert "/spans/" in obj.get_url()

    @pytest.mark.run(order=23)
    def test_navigation_to_cdns(self, driver):
        """测试导航到CDN页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_cdns()
        obj.sleep(2)
        assert "/cdns" in obj.get_url()

    @pytest.mark.run(order=24)
    def test_navigation_to_cdns_purges(self, driver):
        """测试导航到清除 CDN 缓存页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_cdns_purges()
        obj.sleep(2)
        assert "/cdns/purges" in obj.get_url()

    @pytest.mark.run(order=25)
    def test_navigation_to_cdns_prefetches(self, driver):
        """测试导航到内容预取页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_cdns_prefetches()
        obj.sleep(2)
        assert "/cdns/prefetches" in obj.get_url()

    @pytest.mark.run(order=26)
    def test_navigation_to_cdns_domains(self, driver):
        """测试导航到域名管理页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_cdns_domains()
        obj.sleep(2)
        assert "/cdns/domains" in obj.get_url()

    @pytest.mark.run(order=27)
    def test_navigation_to_cdns_certs(self, driver):
        """测试导航到证书页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_cdns_certs()
        obj.sleep(2)
        assert "/cdns/certs" in obj.get_url()

    @pytest.mark.run(order=28)
    def test_navigation_to_dns(self, driver):
        """测试导航到DNS 服务页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_dns()
        obj.sleep(2)
        assert "/dns" in obj.get_url()

    @pytest.mark.run(order=29)
    def test_navigation_to_security_groups(self, driver):
        """测试导航到安全组页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_security_groups()
        obj.sleep(2)
        assert "/security_groups/" in obj.get_url()

    @pytest.mark.run(order=30)
    def test_navigation_to_security_groups_rule_subset(self, driver):
        """测试导航到安全组_规则子集页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_security_groups_rule_subset()
        obj.sleep(2)
        assert "/security_groups/rule_subset/" in obj.get_url()

    @pytest.mark.run(order=31)
    def test_navigation_to_security_groups_security_group_ipsets(self, driver):
        """测试导航到安全组_IP/端口集合页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_security_groups_security_group_ipsets()
        obj.sleep(2)
        assert "/security_groups/security_group_ipsets/" in obj.get_url()

    @pytest.mark.run(order=32)
    def test_navigation_to_security_groups_security_group_ipsets(self, driver):
        """测试导航到网络访问控制页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_network_access_control()
        obj.sleep(2)
        assert "/network_access_control/" in obj.get_url()

    @pytest.mark.run(order=33)
    def test_navigation_to_security_groups_security_group_ipsets(self, driver):
        """测试导航到网络访问控制_基础网络安全策略页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_network_access_control_security_policies()
        obj.sleep(2)
        assert "/network_access_control/security_policies/" in obj.get_url()

    @pytest.mark.run(order=34)
    def test_navigation_to_ssl_certificates(self, driver):
        """测试导航到SSL 证书服务_我的证书页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_ssl_certificates()
        obj.sleep(2)
        assert "/ssl_certificates" in obj.get_url()

    @pytest.mark.run(order=35)
    def test_navigation_to_shared_certificates(self, driver):
        """测试导航到SSL 证书服务_共享证书页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_shared_certificates()
        obj.sleep(2)
        assert "/shared_certificates" in obj.get_url()

    @pytest.mark.run(order=36)
    def test_navigation_to_ssl_orders(self, driver):
        """测试导航到SSL 证书服务_订单列表页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_ssl_orders()
        obj.sleep(2)
        assert "/ssl_orders" in obj.get_url()

    @pytest.mark.run(order=37)
    def test_navigation_to_ddos_defense(self, driver):
        """测试导航到DDoS 攻击防护页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_ddos_defense()
        obj.sleep(2)
        assert "/ddos_defense" in obj.get_url()

    @pytest.mark.run(order=38)
    def test_navigation_to_waf(self, driver):
        """测试导航到Web 应用防火墙（WAF）页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_waf()
        obj.sleep(2)
        assert "/waf/" in obj.get_url()

    @pytest.mark.run(order=39)
    def test_navigation_to_waf_waf_parameter_groups(self, driver):
        """测试导航到WAF 配置组页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_waf_waf_parameter_groups()
        obj.sleep(2)
        assert "/waf/waf_parameter_groups/" in obj.get_url()

    @pytest.mark.run(order=40)
    def test_navigation_to_high_defense(self, driver):
        """测试导航到高防 IP页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_high_defense()
        obj.sleep(2)
        assert "/high_defense/" in obj.get_url()

    @pytest.mark.run(order=41)
    def test_navigation_to_volumes(self, driver):
        """测试导航到硬盘页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_volumes()
        obj.sleep(2)
        assert "/volumes/" in obj.get_url()

    @pytest.mark.run(order=42)
    def test_navigation_to_volumes_reserved_contracts(self, driver):
        """测试导航到硬盘_预留合约页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_volumes_reserved_contracts()
        obj.sleep(2)
        assert "/volumes/reserved_contracts/" in obj.get_url()

    @pytest.mark.run(order=43)
    def test_navigation_to_shared_storage(self, driver):
        """测试导航到共享存储_企业级分布式 SAN (NeonSAN)页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_shared_storage()
        obj.sleep(2)
        assert "/shared_storage/" in obj.get_url()

    @pytest.mark.run(order=44)
    def test_navigation_to_shared_storage_vsans(self, driver):
        """测试导航到共享存储_Virtual SAN（vSAN）页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_shared_storage_vsans()
        obj.sleep(2)
        assert "/shared_storage/vsans/" in obj.get_url()

    @pytest.mark.run(order=45)
    def test_navigation_to_snapshots(self, driver):
        """测试导航到备份_自有备份页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_snapshots()
        obj.sleep(2)
        assert "/snapshots/" in obj.get_url()

    @pytest.mark.run(order=46)
    def test_navigation_to_snapshots_shared(self, driver):
        """测试导航到备份_共享备份页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_snapshots_shared()
        obj.sleep(2)
        assert "/snapshots/shared/" in obj.get_url()

    @pytest.mark.run(order=47)
    def test_navigation_to_qingstor(self, driver):
        """测试导航到对象存储页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_qingstor()
        obj.sleep(2)
        assert "/qingstor/" in obj.get_url()

    @pytest.mark.run(order=48)
    def test_navigation_to_vnass(self, driver):
        """测试导航到文件存储vNAS页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_vnass()
        obj.sleep(2)
        assert "/vnass/" in obj.get_url()

    @pytest.mark.run(order=49)
    def test_navigation_to_s2_groups(self, driver):
        """测试导航到文件存储vNAS_权限组页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_s2_groups()
        obj.sleep(2)
        assert "/s2_groups/" in obj.get_url()

    @pytest.mark.run(order=50)
    def test_navigation_to_s2_accounts(self, driver):
        """测试导航到文件存储vNAS_权限组页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_s2_accounts()
        obj.sleep(2)
        assert "/s2_accounts/" in obj.get_url()

    @pytest.mark.run(order=51)
    def test_navigation_to_wan_nets(self, driver):
        """测试导航到sdwan_企业云网页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_wan_nets()
        obj.sleep(2)
        assert "/wan_nets" in obj.get_url()

    @pytest.mark.run(order=52)
    def test_navigation_to_wan_cpes(self, driver):
        """测试导航到sdwan_光盒页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_wan_cpes()
        obj.sleep(2)
        assert "/wan_cpes" in obj.get_url()

    @pytest.mark.run(order=53)
    def test_navigation_to_wan_gateways(self, driver):
        """测试导航到sdwan_网关页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_wan_gateways()
        obj.sleep(2)
        assert "/wan_gateways" in obj.get_url()

    @pytest.mark.run(order=54)
    def test_navigation_to_wan_lines(self, driver):
        """测试导航到sdwan_专线页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_wan_lines()
        obj.sleep(2)
        assert "/wan_lines" in obj.get_url()

    @pytest.mark.run(order=55)
    def test_navigation_to_wan_global_configs(self, driver):
        """测试导航到sdwan_全局配置_全局配置模板页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_wan_global_configs()
        obj.sleep(2)
        assert "/wan_global_configs" in obj.get_url()

    @pytest.mark.run(order=56)
    def test_navigation_to_wan_global_configs_wan_security_policy(self, driver):
        """测试导航到sdwan_全局配置_安全策略页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_wan_global_configs_wan_security_policy()
        obj.sleep(2)
        assert "/wan_global_configs/wan_security_policy" in obj.get_url()

    @pytest.mark.run(order=57)
    def test_navigation_to_wan_global_configs_wan_device_policy(self, driver):
        """测试导航到sdwan_全局配置_设备策略服务页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_wan_global_configs_wan_device_policy()
        obj.sleep(2)
        assert "/wan_global_configs/wan_device_policy" in obj.get_url()

    @pytest.mark.run(order=58)
    def test_navigation_to_wan_global_configs_wan_resource_set(self, driver):
        """测试导航到sdwan_全局配置_资源配置页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_wan_global_configs_wan_resource_set()
        obj.sleep(2)
        assert "/wan_global_configs/wan_resource_set" in obj.get_url()

    @pytest.mark.run(order=59)
    def test_navigation_to_wan_physical_cpe_orders(self, driver):
        """测试导航到sdwan_物理光盒页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_wan_physical_cpe_orders()
        obj.sleep(2)
        assert "/wan_physical_cpe_orders" in obj.get_url()

    @pytest.mark.run(order=60)
    def test_navigation_to_wan_physical_line_orders(self, driver):
        """测试导航到sdwan_物理专线页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_wan_physical_line_orders()
        obj.sleep(2)
        assert "/wan_physical_line_orders" in obj.get_url()

    @pytest.mark.run(order=61)
    def test_navigation_to_topologies(self, driver):
        """测试导航到运维管理_资源编排_已生成的编排页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_topologies()
        obj.sleep(2)
        assert "/topologies/" in obj.get_url()

    @pytest.mark.run(order=62)
    def test_navigation_to_topology_templates(self, driver):
        """测试导航到运维管理_资源编排_已生成的编排页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_topology_templates()
        obj.sleep(2)
        assert "/topology_templates/" in obj.get_url()

    @pytest.mark.run(order=63)
    def test_navigation_to_autoscaling_policies(self, driver):
        """测试导航到运维管理_自动伸缩页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_autoscaling_policies()
        obj.sleep(2)
        assert "/autoscaling_policies/" in obj.get_url()

    @pytest.mark.run(order=64)
    def test_navigation_to_launch_configurations(self, driver):
        """测试导航到运维管理_自动伸缩_主机启动配置页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_launch_configurations()
        obj.sleep(2)
        assert "/launch_configurations/" in obj.get_url()

    @pytest.mark.run(order=65)
    def test_navigation_to_schedulers(self, driver):
        """测试导航到运维管理_定时器页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_schedulers()
        obj.sleep(2)
        assert "/schedulers/" in obj.get_url()

    @pytest.mark.run(order=66)
    def test_navigation_to_activities(self, driver):
        """测试导航到运维管理_操作日志页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_activities()
        obj.sleep(2)
        assert "/activities/" in obj.get_url()

    @pytest.mark.run(order=67)
    def test_navigation_to_activities_global_jobs(self, driver):
        """测试导航到运维管理_操作日志_全局操作日志页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_activities_global_jobs()
        obj.sleep(2)
        assert "/activities/global_jobs/" in obj.get_url()

    @pytest.mark.run(order=68)
    def test_navigation_to_activities_export(self, driver):
        """测试导航到运维管理_操作日志_导出页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_activities_export()
        obj.sleep(2)
        assert "/activities/export/" in obj.get_url()

    @pytest.mark.run(order=69)
    def test_navigation_to_tags(self, driver):
        """测试导航到运维管理_标签页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_tags()
        obj.sleep(2)
        assert "/tags" in obj.get_url()

    @pytest.mark.run(order=70)
    def test_navigation_to_recyclebin(self, driver):
        """测试导航到运维管理_回收站页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_recyclebin()
        obj.sleep(2)
        assert "/recyclebin/" in obj.get_url()

    @pytest.mark.run(order=71)
    def test_navigation_to_iam_roles(self, driver):
        """测试导航到访问鉴权管理IAM_身份管理页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_iam_roles()
        obj.sleep(2)
        assert "/iam/roles" in obj.get_url()

    @pytest.mark.run(order=72)
    def test_navigation_to_iam_policies(self, driver):
        """测试导航到访问鉴权管理IAM_策略管理页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_iam_policies()
        obj.sleep(2)
        assert "/iam/policies" in obj.get_url()

    @pytest.mark.run(order=73)
    def test_navigation_to_iam_activity(self, driver):
        """测试导航到访问鉴权管理IAM_操作日志页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_iam_activity()
        obj.sleep(2)
        assert "/iam/activity" in obj.get_url()

    @pytest.mark.run(order=74)
    def test_navigation_to_account_security(self, driver):
        """测试导航到账号安全_安全设置页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_account_security()
        obj.sleep(2)
        assert "/account/security" in obj.get_url()

    @pytest.mark.run(order=75)
    def test_navigation_to_account_security_modify_password(self, driver):
        """测试导航到账号安全_修改密码页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_account_security_modify_password()
        obj.sleep(2)
        assert "/account/security/modify_password/" in obj.get_url()

    @pytest.mark.run(order=76)
    def test_navigation_to_account_security_2fa(self, driver):
        """测试导航到账号安全_二次认证页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_account_security_2fa()
        obj.sleep(2)
        assert "/account/security/2fa/" in obj.get_url()

    @pytest.mark.run(order=77)
    def test_navigation_to_account_security_login_history(self, driver):
        """测试导航到账号安全_登录历史页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_account_security_login_history()
        obj.sleep(2)
        assert "/account/security/login_history/" in obj.get_url()

    @pytest.mark.run(order=78)
    def test_navigation_to_account_security_application_authorization(self, driver):
        """测试导航到账号安全_应用授权页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_account_security_application_authorization()
        obj.sleep(2)
        assert "/account/security/application_authorization/" in obj.get_url()

    @pytest.mark.run(order=79)
    def test_navigation_to_subusers(self, driver):
        """测试导航到子账户管理页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_subusers()
        obj.sleep(2)
        assert "/subusers" in obj.get_url()

    @pytest.mark.run(order=80)
    def test_navigation_to_user_groups(self, driver):
        """测试导航到账户组管理页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_user_groups()
        obj.sleep(2)
        assert "/user_groups" in obj.get_url()

    @pytest.mark.run(order=81)
    def test_navigation_to_access_keys(self, driver):
        """测试导航到API 密钥页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_access_keys()
        obj.sleep(2)
        assert "/access_keys" in obj.get_url()

    @pytest.mark.run(order=82)
    def test_navigation_to_apps(self, driver):
        """测试导航到应用中心页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_apps()
        fa = Feature_Action(driver)
        fa.skip()  # 第一次进入app时会弹出引导弹框，这里用于跳过引导
        obj.sleep(2)
        assert "/apps" in obj.get_url()

    @pytest.mark.run(order=83)
    def test_navigation_to_app_mgmt(self, driver):
        """测试导航到应用管理页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_app_mgmt()
        obj.sleep(2)
        assert "/app_mgmt" in obj.get_url()

    @pytest.mark.run(order=84)
    def test_navigation_to_clusters(self, driver):
        """测试导航到集群管理页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_clusters()
        obj.sleep(2)
        assert "/clusters/" in obj.get_url()

    @pytest.mark.run(order=85)
    def test_navigation_to_monitoring_overview(self, driver):
        """测试导航到云监控 CloudSat页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_monitoring_overview()
        obj.sleep(2)
        assert "/monitoring_overview" in obj.get_url()

    @pytest.mark.run(order=86)
    def test_navigation_to_monitors(self, driver):
        """测试导航到云监控 CloudSat_Dashboard页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_monitors()
        obj.sleep(2)
        assert "/monitors" in obj.get_url()

    @pytest.mark.run(order=87)
    def test_navigation_to_resource_groups(self, driver):
        """测试导航到云监控 CloudSat_分组管理页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_resource_groups()
        obj.sleep(2)
        assert "/resource_groups" in obj.get_url()

    @pytest.mark.run(order=88)
    def test_navigation_to_events(self, driver):
        """测试导航到云监控 CloudSat_事件监控页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_events()
        obj.sleep(2)
        assert "/events/" in obj.get_url()

    @pytest.mark.run(order=89)
    def test_navigation_to_alarms(self, driver):
        """测试导航到云监控 CloudSat_告警服务页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_alarms()
        obj.sleep(2)
        assert "/alarms/" in obj.get_url()

    @pytest.mark.run(order=90)
    def test_navigation_to_alarms_custom_alarm_policies(self, driver):
        """测试导航到云监控 CloudSat_告警服务_自定义告警策略页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_alarms_custom_alarm_policies()
        obj.sleep(2)
        assert "/alarms/custom_alarm_policies/" in obj.get_url()

    @pytest.mark.run(order=91)
    def test_navigation_to_custom_monitoring(self, driver):
        """测试导航到云监控 CloudSat_自定义监控页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_custom_monitoring()
        obj.sleep(2)
        assert "/custom_monitoring/" in obj.get_url()

    @pytest.mark.run(order=92)
    def test_navigation_to_container_groups(self, driver):
        """测试导航到弹性容器实例(QCI)页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_container_groups()
        obj.sleep(2)
        assert "/container_groups/" in obj.get_url()

    @pytest.mark.run(order=93)
    def test_navigation_to_image_caches(self, driver):
        """测试导航到容器镜像缓存页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_image_caches()
        obj.sleep(2)
        assert "/image_caches/" in obj.get_url()

    @pytest.mark.run(order=94)
    def test_navigation_to_docker_images(self, driver):
        """测试导航到Docker 镜像仓库页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_docker_images()
        obj.sleep(2)
        assert "/docker_images/docker_repos" in obj.get_url()

    @pytest.mark.run(order=95)
    def test_navigation_to_docker_images_docker_namespaces(self, driver):
        """测试导航到Docker 镜像仓库_命名空间页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_docker_images_docker_namespaces()
        obj.sleep(2)
        assert "/docker_images/docker_namespaces" in obj.get_url()

    @pytest.mark.run(order=96)
    def test_navigation_to_docker_images_docker_users(self, driver):
        """测试导航到Docker 镜像仓库_用户管理页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_docker_images_docker_users()
        obj.sleep(2)
        assert "/docker_images/docker_users" in obj.get_url()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.run(order=97)
    def test_navigation_to_monitoring_status(self, driver):
        """测试导航到监控状态页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_monitoring_status()
        obj.sleep(15)
        assert "https://status.qingcloud.com/" == obj.get_url()
        obj.sleep(2)
        obj.switch_to_window()

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.run(order=98)
    def test_navigation_to_iot(self, driver):
        """测试导航到iot页面是否成功"""
        logger.logger.info('测试用例:【%s】->【%s: %s】' % (
            self.__class__.__name__, getattr(self, p.get_current_function_name()).__doc__,
            p.get_current_function_name()))
        obj = Select_Produce_And_Service_Action(driver)
        obj.navigation_to_iot()
        obj.sleep(15)
        assert "https://iot.console.qingcloud.com/" in obj.get_url()
        obj.sleep(2)
        obj.switch_to_window()


if __name__ == '__main__':
    pytest.main(['-s','test_compute_navigation.py'])
