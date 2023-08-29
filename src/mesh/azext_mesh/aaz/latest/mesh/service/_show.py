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
    "mesh service show",
    is_preview=True,
)
class Show(AAZCommand):
    """Get the details of a service.
    """

    _aaz_info = {
        "version": "2018-09-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.servicefabricmesh/applications/{}/services/{}", "2018-09-01-preview"],
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
        _args_schema.application_name = AAZStrArg(
            options=["--app-name", "--application-name"],
            help="The name of the application.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name  of the service.",
            required=True,
            id_part="child_name_1",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ServiceGet(ctx=self.ctx)()
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

    class ServiceGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationResourceName}/services/{serviceResourceName}",
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
                    "applicationResourceName", self.ctx.args.application_name,
                    skip_quote=True,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "serviceResourceName", self.ctx.args.name,
                    skip_quote=True,
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
                    "api-version", "2018-09-01-preview",
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType()
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.auto_scaling_policies = AAZListType(
                serialized_name="autoScalingPolicies",
            )
            properties.code_packages = AAZListType(
                serialized_name="codePackages",
                flags={"required": True},
            )
            properties.description = AAZStrType()
            properties.diagnostics = AAZObjectType()
            _ShowHelper._build_schema_diagnostics_ref_read(properties.diagnostics)
            properties.health_state = AAZStrType(
                serialized_name="healthState",
            )
            properties.network_refs = AAZListType(
                serialized_name="networkRefs",
            )
            properties.os_type = AAZStrType(
                serialized_name="osType",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.replica_count = AAZIntType(
                serialized_name="replicaCount",
            )
            properties.status = AAZStrType()
            properties.status_details = AAZStrType(
                serialized_name="statusDetails",
                flags={"read_only": True},
            )
            properties.unhealthy_evaluation = AAZStrType(
                serialized_name="unhealthyEvaluation",
                flags={"read_only": True},
            )

            auto_scaling_policies = cls._schema_on_200.properties.auto_scaling_policies
            auto_scaling_policies.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.auto_scaling_policies.Element
            _element.mechanism = AAZObjectType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.trigger = AAZObjectType(
                flags={"required": True},
            )

            mechanism = cls._schema_on_200.properties.auto_scaling_policies.Element.mechanism
            mechanism.kind = AAZStrType(
                flags={"required": True},
            )

            disc_add_remove_replica = cls._schema_on_200.properties.auto_scaling_policies.Element.mechanism.discriminate_by("kind", "AddRemoveReplica")
            disc_add_remove_replica.max_count = AAZIntType(
                serialized_name="maxCount",
                flags={"required": True},
            )
            disc_add_remove_replica.min_count = AAZIntType(
                serialized_name="minCount",
                flags={"required": True},
            )
            disc_add_remove_replica.scale_increment = AAZIntType(
                serialized_name="scaleIncrement",
                flags={"required": True},
            )

            trigger = cls._schema_on_200.properties.auto_scaling_policies.Element.trigger
            trigger.kind = AAZStrType(
                flags={"required": True},
            )

            disc_average_load = cls._schema_on_200.properties.auto_scaling_policies.Element.trigger.discriminate_by("kind", "AverageLoad")
            disc_average_load.lower_load_threshold = AAZFloatType(
                serialized_name="lowerLoadThreshold",
                flags={"required": True},
            )
            disc_average_load.metric = AAZObjectType(
                flags={"required": True},
            )
            disc_average_load.scale_interval_in_seconds = AAZIntType(
                serialized_name="scaleIntervalInSeconds",
                flags={"required": True},
            )
            disc_average_load.upper_load_threshold = AAZFloatType(
                serialized_name="upperLoadThreshold",
                flags={"required": True},
            )

            metric = cls._schema_on_200.properties.auto_scaling_policies.Element.trigger.discriminate_by("kind", "AverageLoad").metric
            metric.kind = AAZStrType(
                flags={"required": True},
            )

            disc_resource = cls._schema_on_200.properties.auto_scaling_policies.Element.trigger.discriminate_by("kind", "AverageLoad").metric.discriminate_by("kind", "Resource")
            disc_resource.name = AAZStrType(
                flags={"required": True},
            )

            code_packages = cls._schema_on_200.properties.code_packages
            code_packages.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.code_packages.Element
            _element.commands = AAZListType()
            _element.diagnostics = AAZObjectType()
            _ShowHelper._build_schema_diagnostics_ref_read(_element.diagnostics)
            _element.endpoints = AAZListType()
            _element.entrypoint = AAZStrType()
            _element.environment_variables = AAZListType(
                serialized_name="environmentVariables",
            )
            _element.image = AAZStrType(
                flags={"required": True},
            )
            _element.image_registry_credential = AAZObjectType(
                serialized_name="imageRegistryCredential",
            )
            _element.instance_view = AAZObjectType(
                serialized_name="instanceView",
            )
            _element.labels = AAZListType()
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.reliable_collections_refs = AAZListType(
                serialized_name="reliableCollectionsRefs",
            )
            _element.resources = AAZObjectType(
                flags={"required": True},
            )
            _element.settings = AAZListType()
            _element.volume_refs = AAZListType(
                serialized_name="volumeRefs",
            )
            _element.volumes = AAZListType()

            commands = cls._schema_on_200.properties.code_packages.Element.commands
            commands.Element = AAZStrType()

            endpoints = cls._schema_on_200.properties.code_packages.Element.endpoints
            endpoints.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.code_packages.Element.endpoints.Element
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.port = AAZIntType()

            environment_variables = cls._schema_on_200.properties.code_packages.Element.environment_variables
            environment_variables.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.code_packages.Element.environment_variables.Element
            _element.name = AAZStrType()
            _element.value = AAZStrType()

            image_registry_credential = cls._schema_on_200.properties.code_packages.Element.image_registry_credential
            image_registry_credential.password = AAZStrType()
            image_registry_credential.server = AAZStrType(
                flags={"required": True},
            )
            image_registry_credential.username = AAZStrType(
                flags={"required": True},
            )

            instance_view = cls._schema_on_200.properties.code_packages.Element.instance_view
            instance_view.current_state = AAZObjectType(
                serialized_name="currentState",
            )
            _ShowHelper._build_schema_container_state_read(instance_view.current_state)
            instance_view.events = AAZListType()
            instance_view.previous_state = AAZObjectType(
                serialized_name="previousState",
            )
            _ShowHelper._build_schema_container_state_read(instance_view.previous_state)
            instance_view.restart_count = AAZIntType(
                serialized_name="restartCount",
            )

            events = cls._schema_on_200.properties.code_packages.Element.instance_view.events
            events.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.code_packages.Element.instance_view.events.Element
            _element.count = AAZIntType()
            _element.first_timestamp = AAZStrType(
                serialized_name="firstTimestamp",
            )
            _element.last_timestamp = AAZStrType(
                serialized_name="lastTimestamp",
            )
            _element.message = AAZStrType()
            _element.name = AAZStrType()
            _element.type = AAZStrType()

            labels = cls._schema_on_200.properties.code_packages.Element.labels
            labels.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.code_packages.Element.labels.Element
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.value = AAZStrType(
                flags={"required": True},
            )

            reliable_collections_refs = cls._schema_on_200.properties.code_packages.Element.reliable_collections_refs
            reliable_collections_refs.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.code_packages.Element.reliable_collections_refs.Element
            _element.do_not_persist_state = AAZBoolType(
                serialized_name="doNotPersistState",
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )

            resources = cls._schema_on_200.properties.code_packages.Element.resources
            resources.limits = AAZObjectType()
            resources.requests = AAZObjectType(
                flags={"required": True},
            )

            limits = cls._schema_on_200.properties.code_packages.Element.resources.limits
            limits.cpu = AAZFloatType()
            limits.memory_in_gb = AAZFloatType(
                serialized_name="memoryInGB",
            )

            requests = cls._schema_on_200.properties.code_packages.Element.resources.requests
            requests.cpu = AAZFloatType(
                flags={"required": True},
            )
            requests.memory_in_gb = AAZFloatType(
                serialized_name="memoryInGB",
                flags={"required": True},
            )

            settings = cls._schema_on_200.properties.code_packages.Element.settings
            settings.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.code_packages.Element.settings.Element
            _element.name = AAZStrType()
            _element.value = AAZStrType()

            volume_refs = cls._schema_on_200.properties.code_packages.Element.volume_refs
            volume_refs.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.code_packages.Element.volume_refs.Element
            _element.destination_path = AAZStrType(
                serialized_name="destinationPath",
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.read_only = AAZBoolType(
                serialized_name="readOnly",
            )

            volumes = cls._schema_on_200.properties.code_packages.Element.volumes
            volumes.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.code_packages.Element.volumes.Element
            _element.creation_parameters = AAZObjectType(
                serialized_name="creationParameters",
                flags={"required": True},
            )
            _element.destination_path = AAZStrType(
                serialized_name="destinationPath",
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.read_only = AAZBoolType(
                serialized_name="readOnly",
            )

            creation_parameters = cls._schema_on_200.properties.code_packages.Element.volumes.Element.creation_parameters
            creation_parameters.description = AAZStrType()
            creation_parameters.kind = AAZStrType(
                flags={"required": True},
            )

            disc_service_fabric_volume_disk = cls._schema_on_200.properties.code_packages.Element.volumes.Element.creation_parameters.discriminate_by("kind", "ServiceFabricVolumeDisk")
            disc_service_fabric_volume_disk.size_disk = AAZStrType(
                serialized_name="sizeDisk",
                flags={"required": True},
            )

            network_refs = cls._schema_on_200.properties.network_refs
            network_refs.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.network_refs.Element
            _element.endpoint_refs = AAZListType(
                serialized_name="endpointRefs",
            )
            _element.name = AAZStrType()

            endpoint_refs = cls._schema_on_200.properties.network_refs.Element.endpoint_refs
            endpoint_refs.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.network_refs.Element.endpoint_refs.Element
            _element.name = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_container_state_read = None

    @classmethod
    def _build_schema_container_state_read(cls, _schema):
        if cls._schema_container_state_read is not None:
            _schema.detail_status = cls._schema_container_state_read.detail_status
            _schema.exit_code = cls._schema_container_state_read.exit_code
            _schema.finish_time = cls._schema_container_state_read.finish_time
            _schema.start_time = cls._schema_container_state_read.start_time
            _schema.state = cls._schema_container_state_read.state
            return

        cls._schema_container_state_read = _schema_container_state_read = AAZObjectType()

        container_state_read = _schema_container_state_read
        container_state_read.detail_status = AAZStrType(
            serialized_name="detailStatus",
        )
        container_state_read.exit_code = AAZStrType(
            serialized_name="exitCode",
        )
        container_state_read.finish_time = AAZStrType(
            serialized_name="finishTime",
        )
        container_state_read.start_time = AAZStrType(
            serialized_name="startTime",
        )
        container_state_read.state = AAZStrType()

        _schema.detail_status = cls._schema_container_state_read.detail_status
        _schema.exit_code = cls._schema_container_state_read.exit_code
        _schema.finish_time = cls._schema_container_state_read.finish_time
        _schema.start_time = cls._schema_container_state_read.start_time
        _schema.state = cls._schema_container_state_read.state

    _schema_diagnostics_ref_read = None

    @classmethod
    def _build_schema_diagnostics_ref_read(cls, _schema):
        if cls._schema_diagnostics_ref_read is not None:
            _schema.enabled = cls._schema_diagnostics_ref_read.enabled
            _schema.sink_refs = cls._schema_diagnostics_ref_read.sink_refs
            return

        cls._schema_diagnostics_ref_read = _schema_diagnostics_ref_read = AAZObjectType()

        diagnostics_ref_read = _schema_diagnostics_ref_read
        diagnostics_ref_read.enabled = AAZBoolType()
        diagnostics_ref_read.sink_refs = AAZListType(
            serialized_name="sinkRefs",
        )

        sink_refs = _schema_diagnostics_ref_read.sink_refs
        sink_refs.Element = AAZStrType()

        _schema.enabled = cls._schema_diagnostics_ref_read.enabled
        _schema.sink_refs = cls._schema_diagnostics_ref_read.sink_refs


__all__ = ["Show"]