# NORNIR-APPS

Pluggable Network CLI tool built on top of Nornir and Napalm

## Why do I need this?

`nornir_apps` is a lightweight wrapper around Nornir and Napalm and it provides a CLI that makes it easy to plugin Nornir-based scripts you have. The ClI tool comes with a few plugins that use the `nornir_napalm` tools that may already be suitable for quick tasks. However, you can easily add to the CLI by writing your own plugin.

## Getting Started

### Installation

Install `nornir_apps` using pip:

```sh
pip install nornir-apps
```

### Configure your Nornir inventory and Initialization config

You can use your existing nornir configuration files and inventory without any modifications. By default, `nornir_apps` looks for a `config.yaml` file in the root of directory from which you're using the `nornir-app` CLI command. You can pass another file using the `-i` or `--init-file` flag as well. You can review sample configuration and inventory files below. They are samples from the [examples](./examples/) directory in the root of this repo.

<details>

  <summary>Sample hosts file</summary>

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

</details>

<details>

  <summary>Sample Groups file</summary>

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

</details>

<details>

  <summary>Nornir Initialization file</summary>

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

</details>

### Getting Started with the CLI

#### View available commands

Use `nornir_apps --help` to view the included commands based on the `napalm_nornir` project. Any plugin that you create and register will show as an available command in the future.

```sh
➜ nornir_app --help

<OUPUT OMMITTED>

Commands:
  napalm-configure  Retrieve device configuration
  napalm-get        Retrieve device configuration using napalm getters
  napalm-ping       Ping device
  napalm-validate   Validate device compliance using napalm_validate
```

#### Examples

```sh
nornir_app -i inventory/config.yaml -h cat9k napalm-ping -d 8.8.8.8
```

> Note: the CLI looks for a `config.yaml` file by default to initiliaze Nornir

If you have a `config.yaml` file present in the current directory, you can omit the `-i` flag:

```sh
nornir_app -h cat9k napalm-ping -d 8.8.8.8
```

The `-h` or `--host-filter` option allows you to pass a simple filter to the inventory for host selection.

```sh
nornir_app -h platform=ios,role=router napalm-ping -d 8.8.8.8
```
