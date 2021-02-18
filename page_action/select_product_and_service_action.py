#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 23:03
# @Author  : Tang Yiwei
# @Email   : 892398433@qq.com
# @File    : select_product_and_service_action.py
# @Software: PyCharm

from page_locators.global_module.global_page import Global_Page

class Select_Produce_And_Service_Action(Global_Page):

    def navigation_to_instance(self):
        """导航到主机服务"""
        self.click_products_and_services()
        self.click_instance_service()

    def navigation_to_instance_reserved_contracts(self):
        """导航到主机_预留合约tab"""
        self.click_products_and_services()
        self.click_instance_service()
        self.click_instance_service_reserved_contract_tab()

    def navigation_to_instance_instance_groups(self):
        """导航到主机的安置策略组tab"""
        self.click_products_and_services()
        self.click_instance_service()
        self.click_instance_service_instance_group_tab()

    def navigation_to_images(self):
        """导航到映像服务"""
        self.click_products_and_services()
        self.click_image_service()

    def navigation_to_image_self(self):
        """导航到映像_自有tab"""
        self.click_products_and_services()
        self.click_image_service()
        self.click_image_service_self_tab()

    def navigation_to_image_shared(self):
        """导航到映像_共享tab"""
        self.click_products_and_services()
        self.click_image_service()
        self.click_image_service_shared_tab()

    def navigation_to_image_market(self):
        """导航到映像_市场tab"""
        self.click_products_and_services()
        self.click_image_service()
        self.click_image_service_market_tab()

    def navigation_to_keypairs(self):
        """导航到SSH密钥服务"""
        self.click_products_and_services()
        self.click_instance_service()
        self.click_keypair_service()

    def navigation_to_devices(self):
        """导航到设备服务"""
        self.click_products_and_services()
        self.click_instance_service()
        self.click_devices_service()

    def navigation_to_nics(self):
        """导航到网卡服务"""
        self.click_products_and_services()
        self.click_instance_service()
        self.click_nics_service()

    def navigation_to_routers(self):
        """导航到VPC服务"""
        self.click_products_and_services()
        self.click_routers_service()

    def navigation_to_loadbalancers(self):
        """导航到负载均衡器服务"""
        self.click_products_and_services()
        self.click_loadbalancers_service()

    def navigation_to_loadbalancers_loadbalancer_policies(self):
        """导航到负载均衡器_转发策略tab"""
        self.click_products_and_services()
        self.click_loadbalancers_service()
        self.click_loadbalancers_service_loadbalancer_policies_tab()

    def navigation_to_loadbalancers_server_certificates(self):
        """导航到负载均衡器_服务器证书tab"""
        self.click_products_and_services()
        self.click_loadbalancers_service()
        self.click_loadbalancers_service_server_certificates_tab()

    def navigation_to_vxnets(self):
        """导航到私有网络服务"""
        self.click_products_and_services()
        self.click_vxnets_service()

    def navigation_to_routing_tables(self):
        """导航到路由表服务"""
        self.click_products_and_services()
        self.click_routers_service()
        self.click_routing_tables_service()

    def navigation_to_eips(self):
        """导航到公网IP服务"""
        self.click_products_and_services()
        self.click_eips_service()

    def navigation_to_eip_v6(self):
        """导航到公网IP_IPv6 tab"""
        self.click_products_and_services()
        self.click_eips_service()
        self.click_eips_service_eip_v6_tab()

    def navigation_to_nfvs(self):
        """导航到NAT网关服务"""
        self.click_products_and_services()
        self.click_nfvs_service()

    def navigation_to_dns_aliases(self):
        """导航到内网域名别名服务"""
        self.click_products_and_services()
        self.click_routers_service()
        self.click_dns_aliases_service()

    def navigation_to_intranet_routers(self):
        """导航到边界路由器服务"""
        self.click_products_and_services()
        self.click_intranet_routers_service()

    def navigation_to_spans(self):
        """导航到网络流量镜像服务"""
        self.click_products_and_services()
        self.click_routers_service()
        self.click_spans_service()

    def navigation_to_cdns(self):
        """导航到CDN服务"""
        self.click_products_and_services()
        self.click_cdns_service()

    def navigation_to_cdns_purges(self):
        """导航到清除 CDN 缓存服务"""
        self.click_products_and_services()
        self.click_cdns_service()
        self.click_cdns_purges_service()

    def navigation_to_cdns_prefetches(self):
        """导航到内容预取服务"""
        self.click_products_and_services()
        self.click_cdns_service()
        self.click_cdns_prefetches_service()

    def navigation_to_cdns_domains(self):
        """导航到域名管理服务"""
        self.click_products_and_services()
        self.click_cdns_service()
        self.click_cdns_domains_service()

    def navigation_to_cdns_certs(self):
        """导航到证书服务"""
        self.click_products_and_services()
        self.click_cdns_service()
        self.click_cdns_certs_service()

    def navigation_to_dns(self):
        """导航到DNS服务"""
        self.click_products_and_services()
        self.click_dns_service()

    def navigation_to_security_groups(self):
        """导航到安全组服务"""
        self.click_products_and_services()
        self.click_security_groups_service()

    def navigation_to_security_groups_rule_subset(self):
        """导航到安全组_规则子集服务"""
        self.click_products_and_services()
        self.click_security_groups_service()
        self.click_security_groups_rule_subset_service()

    def navigation_to_security_groups_security_group_ipsets(self):
        """导航到安全组_IP/端口集合服务"""
        self.click_products_and_services()
        self.click_security_groups_service()
        self.click_security_groups_security_group_ipsets_service()

    def navigation_to_network_access_control(self):
        """导航到网络访问控制服务"""
        self.click_products_and_services()
        self.click_network_access_control_service()

    def navigation_to_network_access_control_security_policies(self):
        """导航到网络访问控制_基础网络安全策略服务"""
        self.click_products_and_services()
        self.click_network_access_control_service()
        self.click_network_access_control_security_policies_service()

    def navigation_to_ssl_certificates(self):
        """导航到我的证书服务"""
        self.click_products_and_services()
        self.click_ssl_certificates_service()

    def navigation_to_shared_certificates(self):
        """导航到共享证书服务"""
        self.click_products_and_services()
        self.click_ssl_certificates_service()
        self.click_shared_certificates_service()

    def navigation_to_ssl_orders(self):
        """导航到订单列表服务"""
        self.click_products_and_services()
        self.click_ssl_certificates_service()
        self.click_ssl_orders_service()

    def navigation_to_ddos_defense(self):
        """导航到DDoS 攻击防护服务"""
        self.click_products_and_services()
        self.click_ddos_defense_service()

    def navigation_to_waf(self):
        """导航到Web 应用防火墙（WAF）服务"""
        self.click_products_and_services()
        self.click_waf_service()

    def navigation_to_waf_waf_parameter_groups(self):
        """导航到WAF 配置组服务"""
        self.click_products_and_services()
        self.click_waf_service()
        self.click_waf_waf_parameter_groups_service()

    def navigation_to_high_defense(self):
        """导航到高防 IP服务"""
        self.click_products_and_services()
        self.click_high_defense_service()

    def navigation_to_volumes(self):
        """导航到硬盘服务"""
        self.click_products_and_services()
        self.click_volumes_service()

    def navigation_to_volumes_reserved_contracts(self):
        """导航到硬盘_预留合约服务"""
        self.click_products_and_services()
        self.click_volumes_service()
        self.click_volumes_reserved_contracts_service()

    def navigation_to_shared_storage(self):
        """导航到共享存储服务"""
        self.click_products_and_services()
        self.click_shared_storage_service()

    def navigation_to_shared_storage_vsans(self):
        """导航到共享存储_Virtual SAN（vSAN）服务"""
        self.click_products_and_services()
        self.click_shared_storage_service()
        self.click_shared_storage_vsans_service()

    def navigation_to_snapshots(self):
        """导航到备份服务"""
        self.click_products_and_services()
        self.click_snapshots_service()

    def navigation_to_snapshots_shared(self):
        """导航到备份_共享备份服务"""
        self.click_products_and_services()
        self.click_snapshots_service()
        self.click_snapshots_shared_service()

    def navigation_to_qingstor(self):
        """导航到对象存储服务"""
        self.click_products_and_services()
        self.click_qingstor_service()

    def navigation_to_vnass(self):
        """导航到文件存储vNAS服务"""
        self.click_products_and_services()
        self.click_vnass_service()

    def navigation_to_s2_groups(self):
        """导航到文件存储vNAS_权限组服务"""
        self.click_products_and_services()
        self.click_vnass_service()
        self.click_s2_groups_service()

    def navigation_to_s2_accounts(self):
        """导航到文件存储vNAS_账户服务"""
        self.click_products_and_services()
        self.click_vnass_service()
        self.click_s2_accounts_service()

    def navigation_to_wan_nets(self):
        """导航到sdwan_企业云网服务"""
        self.click_products_and_services()
        self.click_wan_nets_service()

    def navigation_to_wan_cpes(self):
        """导航到sdwan_光盒服务"""
        self.click_products_and_services()
        self.click_wan_cpes_service()

    def navigation_to_wan_gateways(self):
        """导航到sdwan_网关服务"""
        self.click_products_and_services()
        self.click_wan_gateways_service()

    def navigation_to_wan_lines(self):
        """导航到sdwan_专线服务"""
        self.click_products_and_services()
        self.click_wan_lines_service()

    def navigation_to_wan_global_configs(self):
        """导航到sdwan_全局配置_全局配置模板服务"""
        self.click_products_and_services()
        self.click_wan_nets_service()
        self.click_wan_global_configs_service()

    def navigation_to_wan_global_configs_wan_template(self):
        """导航到sdwan_全局配置_全局配置模板服务"""
        self.click_products_and_services()
        self.click_wan_nets_service()
        self.click_wan_global_configs_wan_template_service()

    def navigation_to_wan_global_configs_wan_security_policy(self):
        """导航到sdwan_全局配置_安全策略服务"""
        self.click_products_and_services()
        self.click_wan_nets_service()
        self.click_wan_global_configs_service()
        self.click_wan_global_configs_wan_security_policy_service()

    def navigation_to_wan_global_configs_wan_device_policy(self):
        """导航到sdwan_全局配置_设备策略服务"""
        self.click_products_and_services()
        self.click_wan_nets_service()
        self.click_wan_global_configs_service()
        self.click_wan_global_configs_wan_device_policy_service()

    def navigation_to_wan_global_configs_wan_resource_set(self):
        """导航到sdwan_全局配置_资源配置服务"""
        self.click_products_and_services()
        self.click_wan_nets_service()
        self.click_wan_global_configs_service()
        self.click_wan_global_configs_wan_resource_set_tab_service()

    def navigation_to_wan_physical_cpe_orders(self):
        """导航到sdwan_物理光盒服务"""
        self.click_products_and_services()
        self.click_wan_nets_service()
        self.click_wan_physical_cpe_orders_service()

    def navigation_to_wan_physical_line_orders(self):
        """导航到sdwan_物理专线服务"""
        self.click_products_and_services()
        self.click_wan_nets_service()
        self.click_wan_physical_line_orders_service()

    def navigation_to_topologies(self):
        """导航到运维管理_资源编排_已生成的编排服务"""
        self.click_products_and_services()
        self.click_topologies_service()

    def navigation_to_topology_templates(self):
        """导航到运维管理_资源编排_编排模板服务"""
        self.click_products_and_services()
        self.click_topologies_service()
        self.click_topology_templates_service()

    def navigation_to_autoscaling_policies(self):
        """导航到运维管理_自动伸缩服务"""
        self.click_products_and_services()
        self.click_autoscaling_policies_service()

    def navigation_to_launch_configurations(self):
        """导航到运维管理_自动伸缩_主机启动配置服务"""
        self.click_products_and_services()
        self.click_autoscaling_policies_service()
        self.click_launch_configurations_service()

    def navigation_to_schedulers(self):
        """导航到运维管理_定时器服务"""
        self.click_products_and_services()
        self.click_schedulers_service()

    def navigation_to_activities(self):
        """导航到运维管理_操作日志服务"""
        self.click_products_and_services()
        self.click_activities_service()

    def navigation_to_activities_global_jobs(self):
        """导航到运维管理_操作日志_全局操作日志服务"""
        self.click_products_and_services()
        self.click_activities_service()
        self.click_activities_global_jobs_service()

    def navigation_to_activities_export(self):
        """导航到运维管理_操作日志_导出服务"""
        self.click_products_and_services()
        self.click_activities_service()
        self.click_activities_export_service()

    def navigation_to_tags(self):
        """导航到运维管理_标签服务"""
        self.click_products_and_services()
        self.click_tags_service()

    def navigation_to_recyclebin(self):
        """导航到运维管理_回收站服务"""
        self.click_products_and_services()
        self.click_recyclebin_service()

    def navigation_to_iam_roles(self):
        """导航到访问鉴权管理IAM_身份管理服务"""
        self.click_products_and_services()
        self.click_iam_roles_service()

    def navigation_to_iam_policies(self):
        """导航到访问鉴权管理IAM_策略管理服务"""
        self.click_products_and_services()
        self.click_iam_roles_service()
        self.click_iam_policies_service()

    def navigation_to_iam_activity(self):
        """导航到访问鉴权管理IAM_操作日志服务"""
        self.click_products_and_services()
        self.click_iam_roles_service()
        self.click_iam_activity_service()

    def navigation_to_account_security(self):
        """导航到账号安全_安全设置服务"""
        self.click_products_and_services()
        self.click_account_security_service()

    def navigation_to_account_security_modify_password(self):
        """导航到账号安全_修改密码服务"""
        self.click_products_and_services()
        self.click_account_security_service()
        self.click_account_security_modify_password_service()

    def navigation_to_account_security_2fa(self):
        """导航到账号安全_二次认证服务"""
        self.click_products_and_services()
        self.click_account_security_service()
        self.click_account_security_2fa_service()

    def navigation_to_account_security_login_history(self):
        """导航到账号安全_登录历史服务"""
        self.click_products_and_services()
        self.click_account_security_service()
        self.click_account_security_login_history_service()

    def navigation_to_account_security_application_authorization(self):
        """导航到账号安全_应用授权服务"""
        self.click_products_and_services()
        self.click_account_security_service()
        self.click_account_security_application_authorization_service()

    def navigation_to_subusers(self):
        """导航到子账户管理服务"""
        self.click_products_and_services()
        self.click_subusers_service()

    def navigation_to_user_groups(self):
        """导航到账户组管理服务"""
        self.click_products_and_services()
        self.click_user_groups_service()

    def navigation_to_access_keys(self):
        """导航到API 密钥服务"""
        self.click_products_and_services()
        self.click_access_keys_service()

    def navigation_to_apps(self):
        """导航到应用中心服务"""
        self.click_products_and_services()
        self.click_apps_service()

    def navigation_to_app_mgmt(self):
        """导航到应用管理服务"""
        self.click_products_and_services()
        self.click_app_mgmt_service()

    def navigation_to_clusters(self):
        """导航到集群管理服务"""
        self.click_products_and_services()
        self.click_clusters_service()

    def navigation_to_monitoring_overview(self):
        """导航到云监控 CloudSat服务"""
        self.click_products_and_services()
        self.click_monitoring_overview_service()

    def navigation_to_monitors(self):
        """导航到云监控 CloudSat_Dashboard服务"""
        self.click_products_and_services()
        self.click_monitoring_overview_service()
        self.click_monitors_service()

    def navigation_to_resource_groups(self):
        """导航到云监控 CloudSat_分组管理服务"""
        self.click_products_and_services()
        self.click_monitoring_overview_service()
        self.click_resource_groups_service()

    def navigation_to_events(self):
        """导航到云监控 CloudSat_事件监控服务"""
        self.click_products_and_services()
        self.click_monitoring_overview_service()
        self.click_events_service()

    def navigation_to_alarms(self):
        """导航到云监控 CloudSat_告警服务"""
        self.click_products_and_services()
        self.click_monitoring_overview_service()
        self.click_alarms_service()

    def navigation_to_alarms_custom_alarm_policies(self):
        """导航到云监控 CloudSat_告警服务_自定义告警策略"""
        self.click_products_and_services()
        self.click_monitoring_overview_service()
        self.click_alarms_service()
        self.click_alarms_custom_alarm_policies_service()

    def navigation_to_custom_monitoring(self):
        """导航到云监控 CloudSat_自定义监控服务"""
        self.click_products_and_services()
        self.click_monitoring_overview_service()
        self.click_custom_monitoring_service()

    def navigation_to_monitoring_status(self):
        """导航到监控状态服务"""
        self.click_products_and_services()
        self.click_monitoring_status_service()

    def navigation_to_iot(self):
        """导航到iot服务"""
        self.click_products_and_services()
        self.click_iot_service()

    def navigation_to_container_groups(self):
        """导航到弹性容器实例(QCI)服务"""
        self.click_products_and_services()
        self.click_container_groups_service()

    def navigation_to_image_caches(self):
        """导航到容器镜像缓存服务"""
        self.click_products_and_services()
        self.click_container_groups_service()
        self.click_image_caches_service()

    def navigation_to_docker_images(self):
        """导航到Docker 镜像仓库服务"""
        self.click_products_and_services()
        self.click_docker_images_service()

    def navigation_to_docker_images_docker_namespaces(self):
        """导航到Docker 镜像仓库_命名空间服务"""
        self.click_products_and_services()
        self.click_docker_images_service()
        self.click_docker_images_docker_namespaces_service()

    def navigation_to_docker_images_docker_users(self):
        """导航到Docker 镜像仓库_用户管理服务"""
        self.click_products_and_services()
        self.click_docker_images_service()
        self.click_docker_images_docker_users_service()









