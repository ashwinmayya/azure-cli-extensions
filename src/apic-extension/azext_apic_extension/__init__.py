# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------
from typing import Type

from azure.cli.core import AzCommandsLoader
from azure.cli.core.aaz import AAZCommand
from azext_apic_extension._help import helps  # pylint: disable=unused-import


class ApicExtensionCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_command_type = CliCommandType(
            operations_tmpl='azext_apic_extension.custom#{}')
        super().__init__(cli_ctx=cli_ctx,
                         custom_command_type=custom_command_type)

    def load_command_table(self, args):
        from azext_apic_extension.commands import load_custom_commands
        from azure.cli.core.aaz import load_aaz_command_table
        try:
            from . import aaz
        except ImportError:
            aaz = None
        if aaz:
            load_aaz_command_table(
                loader=self,
                aaz_pkg_name=aaz.__name__,
                args=args
            )
        load_command_patches(self)
        load_custom_commands(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_apic_extension._params import load_arguments
        load_arguments(self, command)


def is_aaz_command_subclass(value: Type) -> bool:
    return isinstance(value, type) and issubclass(value, AAZCommand)


def load_command_patches(loader: AzCommandsLoader) -> None:
    import inspect
    from azext_apic_extension import command_patches

    for _, value in inspect.getmembers(command_patches):
        # Only load custom commands from the command_patches module
        if is_aaz_command_subclass(value) and value.__module__ == command_patches.__name__:
            if value.AZ_NAME:
                loader.command_table[value.AZ_NAME] = value(loader=loader)


COMMAND_LOADER_CLS = ApicExtensionCommandsLoader
