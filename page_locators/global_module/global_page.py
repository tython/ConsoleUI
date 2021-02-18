#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 15:02
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : global_page.py
# @Software: PyCharm

from common.basepage import BasePage
from conf.settings import CONSOLE_PAGE_ELE
from util.parse_configuration_file import ParseConfigFile

class Global_Page(BasePage):

    parseCF = ParseConfigFile(CONSOLE_PAGE_ELE)
    section_nav_bar = parseCF.getItemSection('nav_bar_page')
    section_search_box = parseCF.getItemSection('search_box_page')
    section_nav_box_selected = parseCF.getItemSection('navigation_bar_page')
    section_products_and_services = parseCF.getItemSection('products_and_services')
    section_table_header = parseCF.getItemSection('server_tables')
    section_feature = parseCF.getItemSection('guide_feature_modal')
    print("开始读取Console Global页面配置文件...\n", section_nav_bar,section_search_box,section_nav_box_selected)

    def click_workbench(self):
        """点击工作台按钮"""
        ele = self.section_nav_bar['global-nav.workbench'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_products_and_services(self):
        """点击产品和服务按钮"""
        ele = self.section_nav_bar['global-nav.products_and_services'.lower()]
        self.wait_ele_visible(ele)
        self.click(ele)

    def click_project(self):
        """点击项目按钮"""
        ele = self.section_nav_bar['global-nav.project'.lower()]
        self.wait_ele_visible(ele)
        self.click(ele)

    def click_search_box(self):
        """点击搜索框按钮"""
        ele = self.section_nav_bar['global-search-box.search'.lower()]
        self.wait_ele_visible(ele)
        self.click(ele)

    def click_resources(self):
        """点击资源按钮"""
        ele = self.section_nav_bar['global-items.resources'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_cost(self):
        """点击费用按钮"""
        ele = self.section_nav_bar['global-items.cost'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_repair(self):
        """点击工单按钮"""
        ele = self.section_nav_bar['global-items.repair'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_alarm(self):
        """点击消息中心按钮"""
        ele = self.section_nav_bar['global-items.alarm'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_account(self):
        """点击账户按钮"""
        ele = self.section_nav_bar['global-nav.account'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def input_search_content_and_enter(self,content):
        """输入检索条件,并点击回车键"""
        ele = self.section_search_box['search_box.input'.lower()]
        self.wait_ele_visible(ele)
        self.input(ele, content)
        self.sleep(1)
        self.enter(ele)

    def click_server_by_name(self,server_name):
        """点击产品与服务的名称"""
        ele = self.wait_ele_visible(self.section_products_and_services['feature_columus'.lower()])
        div_ele = ele.find_elements_by_tag_name('div')
        for i in div_ele:
            dl_ele = i.find_elements_by_tag_name('dl')
            for j in dl_ele:
                dd_ele = j.find_elements_by_tag_name('dd')
                for k in dd_ele:
                    server_name_ele= k.find_element_by_tag_name('a')
                    text = server_name_ele.text
                    if server_name == text:
                        server_name_ele.click()

    def get_page_intro(self):
        """获取服务table的名称"""
        server_table_name = []
        # tab_header = self.findElement('x=>//ul[@class="tab-header"]')
        tab_header = self.wait_ele_visible(self.section_table_header['table_header'.lower()])
        li_ele = tab_header.find_elements_by_tag_name('li')
        for ele in li_ele:
            a_ele = ele.find_element_by_tag_name('a')
            table_name = a_ele.text
            server_table_name.append(table_name)
        return server_table_name

    def click_instance_service(self):
        """点击主机服务"""
        ele = self.section_products_and_services['product.instance'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_instance_service_reserved_contract_tab(self):
        """点击主机页面_预留合约tab"""
        ele = self.section_products_and_services['product.instance.reserved_contract_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_instance_service_instance_group_tab(self):
        """点击主机_安置策略组tab"""
        ele = self.section_products_and_services['product.instance.instance_group_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_image_service(self):
        """点击映像服务"""
        ele = self.section_products_and_services['product.image'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_image_service_self_tab(self):
        """点击映像_自有tab"""
        ele = self.section_products_and_services['product.image_self_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_image_service_shared_tab(self):
        """点击映像_共享tab"""
        ele = self.section_products_and_services['product.image_shared_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_image_service_market_tab(self):
        """点击映像_市场tab"""
        ele = self.section_products_and_services['product.image_market_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_keypair_service(self):
        """点击ssh密钥服务"""
        ele = self.section_products_and_services['product.keypair'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_devices_service(self):
        """点击设备服务"""
        ele = self.section_products_and_services['product.device'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_nics_service(self):
        """点击网卡服务"""
        ele = self.section_products_and_services['product.nic'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_routers_service(self):
        """点击vpc网络"""
        ele = self.section_products_and_services['product.routers'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_loadbalancers_service(self):
        """点击负载均衡器服务"""
        ele = self.section_products_and_services['product.loadbalancers'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_loadbalancers_service_loadbalancer_policies_tab(self):
        """点击负载均衡器_转发策略tab"""
        ele = self.section_products_and_services['product.loadbalancers_loadbalancer_policies_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_loadbalancers_service_server_certificates_tab(self):
        """点击负载均衡器_服务器证书tab"""
        ele = self.section_products_and_services['product.loadbalancers_server_certificates_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_vxnets_service(self):
        """点击私有网络服务"""
        ele = self.section_products_and_services['product.vxnets'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_routing_tables_service(self):
        """点击路由表服务"""
        ele = self.section_products_and_services['product.routing_tables'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_eips_service(self):
        """点击公网IP服务"""
        ele = self.section_products_and_services['product.eips'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_eips_service_eip_v6_tab(self):
        """点击公网IP_IPv6 tab"""
        ele = self.section_products_and_services['product.eips_eip_v6_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_nfvs_service(self):
        """点击NAT网关服务"""
        ele = self.section_products_and_services['product.nfvs'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_dns_aliases_service(self):
        """点击内网域名别名服务"""
        ele = self.section_products_and_services['product.dns_aliases'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_intranet_routers_service(self):
        """点击边界路由器服务"""
        ele = self.section_products_and_services['product.intranet_routers'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_spans_service(self):
        """点击网络流量镜像服务"""
        ele = self.section_products_and_services['product.dns_spans'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_cdns_service(self):
        """点击CDN服务"""
        ele = self.section_products_and_services['product.cdns'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_cdns_purges_service(self):
        """点击清除 CDN 缓存服务"""
        ele = self.section_products_and_services['product.cdns_purges'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_cdns_prefetches_service(self):
        """点击内容预取服务"""
        ele = self.section_products_and_services['product.cdns_prefetches'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_cdns_domains_service(self):
        """点击域名管理服务"""
        ele = self.section_products_and_services['product.cdns_domains'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_cdns_certs_service(self):
        """点击证书服务"""
        ele = self.section_products_and_services['product.cdns_certs'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_dns_service(self):
        """点击DNS服务"""
        ele = self.section_products_and_services['product.dns'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_security_groups_service(self):
        """点击安全组服务"""
        ele = self.section_products_and_services['product.security_groups'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_security_groups_rule_subset_service(self):
        """点击安全组_规则子集服务"""
        ele = self.section_products_and_services['product.security_groups_rule_subset_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_security_groups_security_group_ipsets_service(self):
        """点击安全组_IP/端口集合服务"""
        ele = self.section_products_and_services['product.security_groups_security_group_ipsets_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_network_access_control_service(self):
        """点击网络访问控制服务"""
        ele = self.section_products_and_services['product.network_access_control'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_network_access_control_security_policies_service(self):
        """点击基础网络安全策略服务"""
        ele = self.section_products_and_services['product.network_access_control_security_policies_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_ssl_certificates_service(self):
        """点击SSL 证书服务"""
        ele = self.section_products_and_services['product.ssl_certificates'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_shared_certificates_service(self):
        """点击共享证书服务"""
        ele = self.section_products_and_services['product.shared_certificates'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_ssl_orders_service(self):
        """点击订单列表服务"""
        ele = self.section_products_and_services['product.ssl_orders'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_ddos_defense_service(self):
        """点击DDoS 攻击防护服务"""
        ele = self.section_products_and_services['product.ddos_defense'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_waf_service(self):
        """点击Web 应用防火墙（WAF）服务"""
        ele = self.section_products_and_services['product.waf'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_waf_waf_parameter_groups_service(self):
        """点击WAF 配置组服务"""
        ele = self.section_products_and_services['product.waf_waf_parameter_groups_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_high_defense_service(self):
        """点击高防 IP服务"""
        ele = self.section_products_and_services['product.high_defense'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_volumes_service(self):
        """点击硬盘服务"""
        ele = self.section_products_and_services['product.volumes'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_volumes_reserved_contracts_service(self):
        """点击硬盘_预留合约服务"""
        ele = self.section_products_and_services['product.volumes_reserved_contracts_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_shared_storage_service(self):
        """点击共享存储服务"""
        ele = self.section_products_and_services['product.shared_storage'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_shared_storage_vsans_service(self):
        """点击共享存储_Virtual SAN（vSAN）服务"""
        ele = self.section_products_and_services['product.shared_storage_vsans_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_snapshots_service(self):
        """点击备份服务"""
        ele = self.section_products_and_services['product.snapshots'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_snapshots_shared_service(self):
        """点击备份_共享备份服务"""
        ele = self.section_products_and_services['product.snapshots_shared_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_qingstor_service(self):
        """点击对象存储服务"""
        ele = self.section_products_and_services['product.qingstor'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_vnass_service(self):
        """点击文件存储vNAS服务"""
        ele = self.section_products_and_services['product.vnass'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_s2_groups_service(self):
        """点击权限组服务"""
        ele = self.section_products_and_services['product.s2_groups'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_s2_accounts_service(self):
        """点击账户服务"""
        ele = self.section_products_and_services['product.s2_accounts'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_wan_nets_service(self):
        """点击sdwan_企业云网服务"""
        ele = self.section_products_and_services['product.wan_nets'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_wan_cpes_service(self):
        """点击sdwan_光盒服务"""
        ele = self.section_products_and_services['product.wan_cpes'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_wan_gateways_service(self):
        """点击sdwan_网关服务"""
        ele = self.section_products_and_services['product.wan_gateways'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_wan_lines_service(self):
        """点击sdwan_专线服务"""
        ele = self.section_products_and_services['product.wan_lines'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_wan_global_configs_service(self):
        """点击sdwan_全局配置_全局配置模板服务"""
        ele = self.section_products_and_services['product.wan_global_configs'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_wan_global_configs_wan_template_service(self):
        """点击sdwan_全局配置_全局配置模板服务"""
        ele = self.section_products_and_services['product.wan_global_configs_wan_security_policy_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_wan_global_configs_wan_security_policy_service(self):
        """点击sdwan_全局配置_安全策略服务"""
        ele = self.section_products_and_services['product.wan_global_configs_wan_security_policy_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_wan_global_configs_wan_device_policy_service(self):
        """点击sdwan_全局配置_设备策略服务"""
        ele = self.section_products_and_services['product.wan_global_configs_wan_device_policy_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_wan_global_configs_wan_resource_set_tab_service(self):
        """点击sdwan_全局配置_资源配置服务"""
        ele = self.section_products_and_services['product.wan_global_configs_wan_resource_set_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_wan_physical_cpe_orders_service(self):
        """点击sdwan_物理光盒服务"""
        ele = self.section_products_and_services['product.wan_physical_cpe_orders'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_wan_physical_line_orders_service(self):
        """点击sdwan_物理专线服务"""
        ele = self.section_products_and_services['product.wan_physical_line_orders'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_topologies_service(self):
        """点击运维管理_资源编排_已生成的编排服务"""
        ele = self.section_products_and_services['product.topologies'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_topology_templates_service(self):
        """点击运维管理_资源编排_编排模板服务"""
        ele = self.section_products_and_services['product.topology_templates'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_autoscaling_policies_service(self):
        """点击运维管理_自动伸缩服务"""
        ele = self.section_products_and_services['product.autoscaling_policies'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_launch_configurations_service(self):
        """点击运维管理_自动伸缩_主机启动配置服务"""
        ele = self.section_products_and_services['product.launch_configurations'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_schedulers_service(self):
        """点击运维管理_定时器服务"""
        ele = self.section_products_and_services['product.schedulers'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_activities_service(self):
        """点击运维管理_操作日志服务"""
        ele = self.section_products_and_services['product.activities'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_activities_global_jobs_service(self):
        """点击运维管理_操作日志_全局操作日志服务"""
        ele = self.section_products_and_services['product.activities_global_jobs_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_activities_export_service(self):
        """点击运维管理_操作日志_导出服务"""
        ele = self.section_products_and_services['product.activities_export_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_tags_service(self):
        """点击运维管理_标签服务"""
        ele = self.section_products_and_services['product.tags'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_recyclebin_service(self):
        """点击运维管理_回收站服务"""
        ele = self.section_products_and_services['product.recyclebin'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_iam_roles_service(self):
        """点击访问鉴权管理IAM_身份管理服务"""
        ele = self.section_products_and_services['product.iam_roles'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_iam_policies_service(self):
        """点击访问鉴权管理IAM_策略管理服务"""
        ele = self.section_products_and_services['product.iam_policies'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_iam_activity_service(self):
        """点击访问鉴权管理IAM_操作日志服务"""
        ele = self.section_products_and_services['product.iam_activity'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_account_security_service(self):
        """点击账户安全_安全设置服务"""
        ele = self.section_products_and_services['product.account_security'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_account_security_modify_password_service(self):
        """点击账户安全_修改密码服务"""
        ele = self.section_products_and_services['product.account_security_modify_password_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_account_security_2fa_service(self):
        """点击账户安全_二次认证服务"""
        ele = self.section_products_and_services['product.account_security_2fa_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_account_security_login_history_service(self):
        """点击账户安全_登录历史服务"""
        ele = self.section_products_and_services['product.account_security_login_history_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_account_security_application_authorization_service(self):
        """点击账户安全_应用授权服务"""
        ele = self.section_products_and_services['product.account_security_application_authorization_tab'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_subusers_service(self):
        """点击子账户管理服务"""
        ele = self.section_products_and_services['product.subusers'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_user_groups_service(self):
        """点击账户组管理服务"""
        ele = self.section_products_and_services['product.user_groups'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_access_keys_service(self):
        """点击API 密钥服务"""
        ele = self.section_products_and_services['product.access_keys'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_apps_service(self):
        """点击应用中心服务"""
        ele = self.section_products_and_services['product.apps'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_app_mgmt_service(self):
        """点击应用管理服务"""
        ele = self.section_products_and_services['product.app_mgmt'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_clusters_service(self):
        """点击集群管理服务"""
        ele = self.section_products_and_services['product.clusters'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_monitoring_overview_service(self):
        """点击云监控 CloudSat服务"""
        ele = self.section_products_and_services['product.monitoring_overview'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_monitors_service(self):
        """点击云监控 CloudSat_Dashboard服务"""
        ele = self.section_products_and_services['product.monitors'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_resource_groups_service(self):
        """点击云监控 CloudSat_分组管理服务"""
        ele = self.section_products_and_services['product.resource_groups'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_events_service(self):
        """点击云监控 CloudSat_事件监控服务"""
        ele = self.section_products_and_services['product.events'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_alarms_service(self):
        """点击云监控 CloudSat_告警服务服务"""
        ele = self.section_products_and_services['product.alarms'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_alarms_custom_alarm_policies_service(self):
        """点击云监控 CloudSat_告警服务_自定义告警策略服务"""
        ele = self.section_products_and_services['product.alarms_custom_alarm_policies'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_custom_monitoring_service(self):
        """点击云监控 CloudSat_自定义监控服务"""
        ele = self.section_products_and_services['product.custom_monitoring'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_monitoring_status_service(self):
        """点击监控状态服务"""
        ele = self.section_products_and_services['product.monitoring_status'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.switch_to_window(ele)

    def click_iot_service(self):
        """点击iot服务"""
        ele = self.section_products_and_services['product.iot'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.switch_to_window(ele)

    def click_container_groups_service(self):
        """点击弹性容器实例(QCI)服务"""
        ele = self.section_products_and_services['product.container_groups'.lower()]
        self.wait_ele_visible(ele)
        self.scroll_element(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_image_caches_service(self):
        """点击容器镜像缓存服务"""
        ele = self.section_products_and_services['product.image_caches'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_docker_images_service(self):
        """点击Docker 镜像仓库服务"""
        ele = self.section_products_and_services['product.docker_images'.lower()]
        self.wait_ele_visible(ele)
        self.scroll_element(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_docker_images_docker_namespaces_service(self):
        """点击Docker 镜像仓库_命名空间服务"""
        ele = self.section_products_and_services['product.docker_images_docker_namespaces'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)

    def click_docker_images_docker_users_service(self):
        """点击Docker 镜像仓库_用户管理服务"""
        ele = self.section_products_and_services['product.docker_images_docker_users'.lower()]
        self.wait_ele_visible(ele)
        self.move_to_element(ele)
        self.click(ele)


if __name__ == '__main__':
    from common.driver import browser
    from conf.settings import CONSOLE_HOST_INFO
    from page_action.login_action import Login_Action
    driver = browser()
    driver.get(CONSOLE_HOST_INFO['testing'])
    obj = Login_Action(driver)
    obj.console_login("tyw2@yunify.com","QingCloud.123")

    obj2 = Global_Page(driver)
    obj2.click_products_and_services()
    obj2.click_server_by_name('硬盘')
    obj2.get_page_intro()

