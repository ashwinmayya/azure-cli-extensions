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
    "self-help simplified-solution show",
    is_preview=True,
)
class Show(AAZCommand):
    """Get the solution using the applicable solutionResourceName while creating the solution.

    :example: Show Solution at Resource Level
        az self-help simplified-solution show --solution-name solution-name --scope 'subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myresourceGroup/providers/Microsoft.KeyVault/vaults/test-keyvault-non-read'
    """

    _aaz_info = {
        "version": "2024-03-01-preview",
        "resources": [
            ["mgmt-plane", "/{scope}/providers/microsoft.help/simplifiedsolutions/{}", "2024-03-01-preview"],
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
        _args_schema.scope = AAZStrArg(
            options=["--scope"],
            help="This is an extension resource provider and only resource level extension is supported at the moment.",
            required=True,
        )
        _args_schema.solution_name = AAZStrArg(
            options=["--solution-name"],
            help="Solution resource Name.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[A-Za-z0-9-+@()_]+$",
                max_length=100,
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SolutionGet(ctx=self.ctx)()
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

    class SolutionGet(AAZHttpOperation):
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
                "/{scope}/providers/Microsoft.Help/simplifiedsolutions/{solutionResourceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "scope", self.ctx.args.scope,
                    skip_quote=True,
                    required=True,
                ),
                **self.serialize_url_param(
                    "solutionResourceName", self.ctx.args.solution_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01-preview",
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
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.content = AAZStrType()
            properties.parameters = AAZDictType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            
            properties.solution_id = AAZStrType(
                serialized_name="solutionId",
            )
            properties.title = AAZStrType()

            parameters = cls._schema_on_200.properties.parameters
            parameters.Element = AAZStrType()

            return cls._schema_on_200

__all__ = ["Show"]
