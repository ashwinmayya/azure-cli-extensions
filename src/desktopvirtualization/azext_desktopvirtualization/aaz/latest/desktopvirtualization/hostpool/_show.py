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
    "desktopvirtualization hostpool show",
)
class Show(AAZCommand):
    """Show a host pool.

    :example: Show host pool
        az desktopvirtualization hostpool show -g rg -n hostpool-name
    """

    _aaz_info = {
        "version": "2021-07-12",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.desktopvirtualization/hostpools/{}", "2021-07-12"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of the host pool within the specified resource group",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                max_length=64,
                min_length=3,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.HostPoolsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class HostPoolsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}",
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
                    "hostPoolName", self.ctx.args.name,
                    required=True,
                ),
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
            _schema_on_200.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.kind = AAZStrType()
            _schema_on_200.location = AAZStrType()
            _schema_on_200.managed_by = AAZStrType(
                serialized_name="managedBy",
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.plan = AAZObjectType()
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.sku = AAZObjectType()
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()

            plan = cls._schema_on_200.plan
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

            properties = cls._schema_on_200.properties
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

            application_group_references = cls._schema_on_200.properties.application_group_references
            application_group_references.Element = AAZStrType()

            migration_request = cls._schema_on_200.properties.migration_request
            migration_request.migration_path = AAZStrType(
                serialized_name="migrationPath",
            )
            migration_request.operation = AAZStrType()

            registration_info = cls._schema_on_200.properties.registration_info
            registration_info.expiration_time = AAZStrType(
                serialized_name="expirationTime",
            )
            registration_info.registration_token_operation = AAZStrType(
                serialized_name="registrationTokenOperation",
            )
            registration_info.token = AAZStrType()

            sku = cls._schema_on_200.sku
            sku.capacity = AAZIntType()
            sku.family = AAZStrType()
            sku.name = AAZStrType(
                flags={"required": True},
            )
            sku.size = AAZStrType()
            sku.tier = AAZStrType()

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
