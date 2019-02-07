---
config:
    plugin_type: install
subparsers:
    rhhi:
        description: Configure RHHI environment
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Hypervisor
              options:
                  vbmc-username:
                      type: Value
                      default: admin
                      help: |
                          VBMC username (Relevant when Ironic's driver is 'pxe_ipmitool' - OSP >= 11)
                          NOTE: If you use non default value for the option, and you execute introspection
                          and deploy (--introspect yes/--deploy yes) in different IR runs, you need to provide
                          the option on both runs.
                  vbmc-password:
                      type: Value
                      default: password
                      help: |
                          VBMC password (Relevant when Ironic's driver is 'pxe_ipmitool' - OSP >= 11)
                          NOTE: If you use non default value for the option, and you execute introspection
                          and deploy (--introspect yes/--deploy yes) in different IR runs, you need to provide
                          the option on both runs.
                  vbmc-host:
                      type: Value
                      default: hypervisor
                      choices:
                          - "hypervisor"
                      help: |
                          Specifies on what server the virtualbmc service should be installed.
                          NOTE: If you use non default value for the option, and you execute introspection
                          and deploy (--introspect yes/--deploy yes) in different IR runs, you need to provide
                          the option on both runs.
                  pullsecret:
                      type: Value
                      default: ''
