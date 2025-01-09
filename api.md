# Accounts

Types:

```python
from fireapi_v2.types import AccountInfo
```

Methods:

- <code title="get /api/account">client.accounts.<a href="./src/fireapi_v2/resources/accounts/accounts.py">retrieve</a>() -> <a href="./src/fireapi_v2/types/account_info.py">AccountInfo</a></code>

## Services

Types:

```python
from fireapi_v2.types.accounts import ServiceListResponse
```

Methods:

- <code title="get /api/account/services">client.accounts.services.<a href="./src/fireapi_v2/resources/accounts/services.py">list</a>() -> <a href="./src/fireapi_v2/types/accounts/service_list_response.py">object</a></code>

## Donations

Types:

```python
from fireapi_v2.types.accounts import DonationListResponse
```

Methods:

- <code title="get /api/account/donations">client.accounts.donations.<a href="./src/fireapi_v2/resources/accounts/donations.py">list</a>() -> <a href="./src/fireapi_v2/types/accounts/donation_list_response.py">object</a></code>

## Affiliate

Types:

```python
from fireapi_v2.types.accounts import AffiliateRetrieveResponse
```

Methods:

- <code title="get /api/account/affiliate">client.accounts.affiliate.<a href="./src/fireapi_v2/resources/accounts/affiliate.py">retrieve</a>() -> <a href="./src/fireapi_v2/types/accounts/affiliate_retrieve_response.py">object</a></code>

# Domains

Types:

```python
from fireapi_v2.types import DomainRetrieveResponse
```

Methods:

- <code title="get /api/domain/{internal_id}">client.domains.<a href="./src/fireapi_v2/resources/domains/domains.py">retrieve</a>(internal_id) -> <a href="./src/fireapi_v2/types/domain_retrieve_response.py">object</a></code>

## DNS

Types:

```python
from fireapi_v2.types.domains import (
    DNSRetrieveResponse,
    DNSAddResponse,
    DNSEditResponse,
    DNSRemoveResponse,
)
```

Methods:

- <code title="get /api/domain/{internal_id}/dns">client.domains.dns.<a href="./src/fireapi_v2/resources/domains/dns.py">retrieve</a>(internal_id) -> <a href="./src/fireapi_v2/types/domains/dns_retrieve_response.py">object</a></code>
- <code title="put /api/domain/{internal_id}/dns/add">client.domains.dns.<a href="./src/fireapi_v2/resources/domains/dns.py">add</a>(internal_id, \*\*<a href="src/fireapi_v2/types/domains/dns_add_params.py">params</a>) -> <a href="./src/fireapi_v2/types/domains/dns_add_response.py">object</a></code>
- <code title="post /api/domain/{internal_id}/dns/edit">client.domains.dns.<a href="./src/fireapi_v2/resources/domains/dns.py">edit</a>(internal_id, \*\*<a href="src/fireapi_v2/types/domains/dns_edit_params.py">params</a>) -> <a href="./src/fireapi_v2/types/domains/dns_edit_response.py">object</a></code>
- <code title="delete /api/domain/{internal_id}/dns/remove">client.domains.dns.<a href="./src/fireapi_v2/resources/domains/dns.py">remove</a>(internal_id, \*\*<a href="src/fireapi_v2/types/domains/dns_remove_params.py">params</a>) -> <a href="./src/fireapi_v2/types/domains/dns_remove_response.py">object</a></code>

# Kvms

## Backup

Types:

```python
from fireapi_v2.types.kvms import BackupListResponse
```

Methods:

- <code title="get /api/kvm/{internal_id}/backup/list">client.kvms.backup.<a href="./src/fireapi_v2/resources/kvms/backup.py">list</a>(internal_id) -> <a href="./src/fireapi_v2/types/kvms/backup_list_response.py">object</a></code>

# Kvm

Types:

```python
from fireapi_v2.types import KvmPowerResponse
```

Methods:

- <code title="post /api/kvm/{internal_id}/power">client.kvm.<a href="./src/fireapi_v2/resources/kvm/kvm.py">power</a>(internal_id, \*\*<a href="src/fireapi_v2/types/kvm_power_params.py">params</a>) -> <a href="./src/fireapi_v2/types/kvm_power_response.py">object</a></code>

## Backup

Types:

```python
from fireapi_v2.types.kvm import (
    BackupCreateResponse,
    BackupDeleteResponse,
    BackupCreateStatusResponse,
    BackupRestoreResponse,
    BackupRestoreStatusResponse,
)
```

Methods:

- <code title="post /api/kvm/{internal_id}/backup/create">client.kvm.backup.<a href="./src/fireapi_v2/resources/kvm/backup.py">create</a>(internal_id, \*\*<a href="src/fireapi_v2/types/kvm/backup_create_params.py">params</a>) -> <a href="./src/fireapi_v2/types/kvm/backup_create_response.py">object</a></code>
- <code title="delete /api/kvm/{internal_id}/backup/delete">client.kvm.backup.<a href="./src/fireapi_v2/resources/kvm/backup.py">delete</a>(internal_id, \*\*<a href="src/fireapi_v2/types/kvm/backup_delete_params.py">params</a>) -> <a href="./src/fireapi_v2/types/kvm/backup_delete_response.py">object</a></code>
- <code title="post /api/kvm/{internal_id}/backup/create/status">client.kvm.backup.<a href="./src/fireapi_v2/resources/kvm/backup.py">create_status</a>(internal_id, \*\*<a href="src/fireapi_v2/types/kvm/backup_create_status_params.py">params</a>) -> <a href="./src/fireapi_v2/types/kvm/backup_create_status_response.py">object</a></code>
- <code title="post /api/kvm/{internal_id}/backup/restore">client.kvm.backup.<a href="./src/fireapi_v2/resources/kvm/backup.py">restore</a>(internal_id, \*\*<a href="src/fireapi_v2/types/kvm/backup_restore_params.py">params</a>) -> <a href="./src/fireapi_v2/types/kvm/backup_restore_response.py">object</a></code>
- <code title="post /api/kvm/{internal_id}/backup/restore/status">client.kvm.backup.<a href="./src/fireapi_v2/resources/kvm/backup.py">restore_status</a>(internal_id, \*\*<a href="src/fireapi_v2/types/kvm/backup_restore_status_params.py">params</a>) -> <a href="./src/fireapi_v2/types/kvm/backup_restore_status_response.py">object</a></code>

## Traffic

Types:

```python
from fireapi_v2.types.kvm import TrafficRetrieveResponse, TrafficChartResponse, TrafficLogResponse
```

Methods:

- <code title="get /api/kvm/{internal_id}/traffic/current">client.kvm.traffic.<a href="./src/fireapi_v2/resources/kvm/traffic.py">retrieve</a>(internal_id) -> <a href="./src/fireapi_v2/types/kvm/traffic_retrieve_response.py">object</a></code>
- <code title="post /api/kvm/{internal_id}/traffic/chart">client.kvm.traffic.<a href="./src/fireapi_v2/resources/kvm/traffic.py">chart</a>(internal_id, \*\*<a href="src/fireapi_v2/types/kvm/traffic_chart_params.py">params</a>) -> <a href="./src/fireapi_v2/types/kvm/traffic_chart_response.py">object</a></code>
- <code title="get /api/kvm/{internal_id}/traffic/log">client.kvm.traffic.<a href="./src/fireapi_v2/resources/kvm/traffic.py">log</a>(internal_id) -> <a href="./src/fireapi_v2/types/kvm/traffic_log_response.py">object</a></code>

## Monitoring

Types:

```python
from fireapi_v2.types.kvm import MonitoringIncidencesResponse, MonitoringTimingsResponse
```

Methods:

- <code title="get /api/kvm/{internal_id}/monitoring/incidences">client.kvm.monitoring.<a href="./src/fireapi_v2/resources/kvm/monitoring.py">incidences</a>(internal_id) -> <a href="./src/fireapi_v2/types/kvm/monitoring_incidences_response.py">object</a></code>
- <code title="get /api/kvm/{internal_id}/monitoring/timings">client.kvm.monitoring.<a href="./src/fireapi_v2/resources/kvm/monitoring.py">timings</a>(internal_id) -> <a href="./src/fireapi_v2/types/kvm/monitoring_timings_response.py">object</a></code>

## Ddos

Types:

```python
from fireapi_v2.types.kvm import DdoRetrieveResponse, DdoChangeResponse
```

Methods:

- <code title="get /api/kvm/{internal_id}/ddos">client.kvm.ddos.<a href="./src/fireapi_v2/resources/kvm/ddos.py">retrieve</a>(internal_id) -> <a href="./src/fireapi_v2/types/kvm/ddo_retrieve_response.py">object</a></code>
- <code title="post /api/kvm/{internal_id}/ddos/change">client.kvm.ddos.<a href="./src/fireapi_v2/resources/kvm/ddos.py">change</a>(internal_id, \*\*<a href="src/fireapi_v2/types/kvm/ddo_change_params.py">params</a>) -> <a href="./src/fireapi_v2/types/kvm/ddo_change_response.py">object</a></code>

## Config

Types:

```python
from fireapi_v2.types.kvm import ConfigRetrieveResponse
```

Methods:

- <code title="get /api/kvm/{internal_id}/config">client.kvm.config.<a href="./src/fireapi_v2/resources/kvm/config.py">retrieve</a>(internal_id) -> <a href="./src/fireapi_v2/types/kvm/config_retrieve_response.py">object</a></code>

## Status

Types:

```python
from fireapi_v2.types.kvm import StatusRetrieveResponse
```

Methods:

- <code title="get /api/kvm/{internal_id}/status">client.kvm.status.<a href="./src/fireapi_v2/resources/kvm/status.py">retrieve</a>(internal_id) -> <a href="./src/fireapi_v2/types/kvm/status_retrieve_response.py">object</a></code>

# Webspaces

Types:

```python
from fireapi_v2.types import WebspaceRetrieveResponse
```

Methods:

- <code title="get /api/webspace/{internal_id}">client.webspaces.<a href="./src/fireapi_v2/resources/webspaces.py">retrieve</a>(internal_id) -> <a href="./src/fireapi_v2/types/webspace_retrieve_response.py">object</a></code>
