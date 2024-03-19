# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "desktopvirtualization hostpool list",
)
class List(AAZCommand):
    """List host pools.

    :example: List host pool
        az desktopvirtualization hostpool list -g rg
    """

    _aaz_info = {
        "version": "2021-07-12",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.desktopvirtualization/hostpools", "2021-07-12"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.desktopvirtualization/hostpools", "2021-07-12"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        condition_1 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        if condition_0:
            self.HostPoolsList(ctx=self.ctx)()
        if condition_1:
            self.HostPoolsListByResourceGroup(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class HostPoolsList(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.DesktopVirtualization/hostPools",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-07-12",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.kind = AAZStrType()
            _element.location = AAZStrType()
            _element.managed_by = AAZStrType(
                serialized_name="managedBy",
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.plan = AAZObjectType()
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()

            plan = cls._schema_on_200.value.Element.plan
            plan.name = AAZStrType(
                flags={"required": True},
            )
            plan.product = AAZStrType(
                flags={"required": True},
            )
            plan.promotion_code = AAZStrType(
                serialized_name="promotionCode",
            )
            plan.publisher = AAZStrType(
                flags={"required": True},
            )
            plan.version = AAZStrType()

            properties = cls._schema_on_200.value.Element.properties
            properties.application_group_references = AAZListType(
                serialized_name="applicationGroupReferences",
                flags={"read_only": True},
            )
            properties.cloud_pc_resource = AAZBoolType(
                serialized_name="cloudPcResource",
                flags={"read_only": True},
            )
            properties.custom_rdp_property = AAZStrType(
                serialized_name="customRdpProperty",
            )
            properties.description = AAZStrType()
            properties.friendly_name = AAZStrType(
                serialized_name="friendlyName",
            )
            properties.host_pool_type = AAZStrType(
                serialized_name="hostPoolType",
                flags={"required": True},
            )
            properties.load_balancer_type = AAZStrType(
                serialized_name="loadBalancerType",
                flags={"required": True},
            )
            properties.max_session_limit = AAZIntType(
                serialized_name="maxSessionLimit",
            )
            properties.migration_request = AAZObjectType(
                serialized_name="migrationRequest",
            )
            properties.object_id = AAZStrType(
                serialized_name="objectId",
                flags={"read_only": True},
            )
            properties.personal_desktop_assignment_type = AAZStrType(
                serialized_name="personalDesktopAssignmentType",
            )
            properties.preferred_app_group_type = AAZStrType(
                serialized_name="preferredAppGroupType",
                flags={"required": True},
            )
            properties.registration_info = AAZObjectType(
                serialized_name="registrationInfo",
            )
            properties.ring = AAZIntType()
            properties.sso_client_id = AAZStrType(
                serialized_name="ssoClientId",
            )
            properties.sso_client_secret_key_vault_path = AAZStrType(
                serialized_name="ssoClientSecretKeyVaultPath",
            )
            properties.sso_secret_type = AAZStrType(
                serialized_name="ssoSecretType",
            )
            properties.ssoadfs_authority = AAZStrType(
                serialized_name="ssoadfsAuthority",
            )
            properties.start_vm_on_connect = AAZBoolType(
                serialized_name="startVMOnConnect",
            )
            properties.validation_environment = AAZBoolType(
                serialized_name="validationEnvironment",
            )
            properties.vm_template = AAZStrType(
                serialized_name="vmTemplate",
            )

            application_group_references = cls._schema_on_200.value.Element.properties.application_group_references
            application_group_references.Element = AAZStrType()

            migration_request = cls._schema_on_200.value.Element.properties.migration_request
            migration_request.migration_path = AAZStrType(
                serialized_name="migrationPath",
            )
            migration_request.operation = AAZStrType()

            registration_info = cls._schema_on_200.value.Element.properties.registration_info
            registration_info.expiration_time = AAZStrType(
                serialized_name="expirationTime",
            )
            registration_info.registration_token_operation = AAZStrType(
                serialized_name="registrationTokenOperation",
            )
            registration_info.token = AAZStrType()

            sku = cls._schema_on_200.value.Element.sku
            sku.capacity = AAZIntType()
            sku.family = AAZStrType()
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.size = AAZStrType()
            sku.tier = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class HostPoolsListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-07-12",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.etag = AAZStrType(
                flags={"read_only": True},
            )
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.kind = AAZStrType()
            _element.location = AAZStrType()
            _element.managed_by = AAZStrType(
                serialized_name="managedBy",
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.plan = AAZObjectType()
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()

            plan = cls._schema_on_200.value.Element.plan
            plan.name = AAZStrType(
                flags={"required": True},
            )
            plan.product = AAZStrType(
                flags={"required": True},
            )
            plan.promotion_code = AAZStrType(
                serialized_name="promotionCode",
            )
            plan.publisher = AAZStrType(
                flags={"required": True},
            )
            plan.version = AAZStrType()

            properties = cls._schema_on_200.value.Element.properties
            properties.application_group_references = AAZListType(
                serialized_name="applicationGroupReferences",
                flags={"read_only": True},
            )
            properties.cloud_pc_resource = AAZBoolType(
                serialized_name="cloudPcResource",
                flags={"read_only": True},
            )
            properties.custom_rdp_property = AAZStrType(
                serialized_name="customRdpProperty",
            )
            properties.description = AAZStrType()
            properties.friendly_name = AAZStrType(
                serialized_name="friendlyName",
            )
            properties.host_pool_type = AAZStrType(
                serialized_name="hostPoolType",
                flags={"required": True},
            )
            properties.load_balancer_type = AAZStrType(
                serialized_name="loadBalancerType",
                flags={"required": True},
            )
            properties.max_session_limit = AAZIntType(
                serialized_name="maxSessionLimit",
            )
            properties.migration_request = AAZObjectType(
                serialized_name="migrationRequest",
            )
            properties.object_id = AAZStrType(
                serialized_name="objectId",
                flags={"read_only": True},
            )
            properties.personal_desktop_assignment_type = AAZStrType(
                serialized_name="personalDesktopAssignmentType",
            )
            properties.preferred_app_group_type = AAZStrType(
                serialized_name="preferredAppGroupType",
                flags={"required": True},
            )
            properties.registration_info = AAZObjectType(
                serialized_name="registrationInfo",
            )
            properties.ring = AAZIntType()
            properties.sso_client_id = AAZStrType(
                serialized_name="ssoClientId",
            )
            properties.sso_client_secret_key_vault_path = AAZStrType(
                serialized_name="ssoClientSecretKeyVaultPath",
            )
            properties.sso_secret_type = AAZStrType(
                serialized_name="ssoSecretType",
            )
            properties.ssoadfs_authority = AAZStrType(
                serialized_name="ssoadfsAuthority",
            )
            properties.start_vm_on_connect = AAZBoolType(
                serialized_name="startVMOnConnect",
            )
            properties.validation_environment = AAZBoolType(
                serialized_name="validationEnvironment",
            )
            properties.vm_template = AAZStrType(
                serialized_name="vmTemplate",
            )

            application_group_references = cls._schema_on_200.value.Element.properties.application_group_references
            application_group_references.Element = AAZStrType()

            migration_request = cls._schema_on_200.value.Element.properties.migration_request
            migration_request.migration_path = AAZStrType(
                serialized_name="migrationPath",
            )
            migration_request.operation = AAZStrType()

            registration_info = cls._schema_on_200.value.Element.properties.registration_info
            registration_info.expiration_time = AAZStrType(
                serialized_name="expirationTime",
            )
            registration_info.registration_token_operation = AAZStrType(
                serialized_name="registrationTokenOperation",
            )
            registration_info.token = AAZStrType()

            sku = cls._schema_on_200.value.Element.sku
            sku.capacity = AAZIntType()
            sku.family = AAZStrType()
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.size = AAZStrType()
            sku.tier = AAZStrType()

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
