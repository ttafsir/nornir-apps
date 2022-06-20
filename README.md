# NRCLI

Pluggable Network CLI tool built on top of Nornir and Napalm

## Why do I need this?

`nrcli` is a lightweight wrapper around Nornir and Napalm and it provides a CLI that makes it easy to plugin Nornir-based scripts you have. The ClI tool comes with a few plugins that use the `nornir_napalm` tools that may already be suitable for quick tasks. However, you can easily add to the CLI by writing your own plugin.

## Getting Started

### Installation

Install `nrcli` using pip:

```sh
pip install nrcli
```

### Configure your Nornir inventory and Initialization config

#### Sample hosts file

```yaml
# examples/inventory/hosts.yaml
cat9k:
  hostname: 10.253.175.87
  port: 22
  username: cisco
  password: cisco
  groups:
    - cisco_iosxe
```

#### Sample Groups file

```yaml
# examples/inventory/groups.yaml
---
cisco_iosxe:
  platform: ios
  data:
    role: router
  connection_options:
    napalm:
      extras:
        optional_args:
          fast_cli: False
          secret: cisco
          conn_timeout: 30
```

### Nornir Initialization file

```yaml
---
core:
  raise_on_error: False

runner:
  plugin: threaded
  options:
    num_workers: 100

logging:
  enabled: True

inventory:
  plugin: SimpleInventory
  options:
    host_file: "inventory/hosts.yaml"
    group_file: "inventory/groups.yaml"
    defaults_file: "inventory/defaults.yaml"
```

### Use the CLI

#### View available commands

Use `nrcli --help` to view the included commands based on the `napalm_nornir` project. Any plugin that you create and register will show as an available command in the future.

```sh
➜ nrcli --help

<OUPUT OMMITTED>

Commands:
  napalm-configure  Retrieve device configuration
  napalm-get        Retrieve device configuration using napalm getters
  napalm-ping       Ping device
  napalm-validate   Validate device compliance using napalm_validate
```

#### Examples

```sh
nrcli -i inventory/config.yaml -h cat9k napalm-ping -d 8.8.8.8
```

> Note: the CLI looks for a `config.yaml` file by default to initiliaze Nornir

If you have a `config.yaml` file present, you can simply try:

```sh
nrcli --host-filter cat9k napalm-ping -d 8.8.8.8
```

The `-h` or `--host-filter` option allows you to pass a simple filter to the inventory for host selection.

```sh
nrcli -h platform=ios,role=router napalm-ping -d 8.8.8.8
```
