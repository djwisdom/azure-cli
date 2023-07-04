# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------
# swagger change: https://github.com/Azure/azure-rest-api-specs/pull/24526

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "network lb",
)
class __CMDGroup(AAZCommandGroup):
    """Manage and configure load balancers.

    To learn more about Azure Load Balancer visit https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-cli.
    """
    pass


__all__ = ["__CMDGroup"]
