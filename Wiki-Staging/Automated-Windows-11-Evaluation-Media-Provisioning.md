# Automated Windows 11 Evaluation Media Provisioning

To maintain an ultra-lightweight repository size under 10MB while supporting high-density 5.4GB OS deployments, this range uses a **Dynamic Web Seed Mapping** module.

## ⚙️ Automated ISO Ingestion
Instead of forcing manual web registration forms or handling massive file attachments, users run our native background downloader tool directly inside the repository directory cache lane.

```powershell
# Navigate into the ISO folder and unleash the background stream engine
cd ./02-ISO-Archive
.\Fetch-Windows11-ISO.ps1
```

## 🛡️ Target Integrity Mapped
* **Source Authenticity**: Streams directly via Microsoft's secure Azure/Prss content delivery network nodes (`://microsoft.com`).
* **Licensing Compliance**: Installs a pristine, fully legal **90-Day Enterprise Evaluation** instance that requires zero product activation keys or commercial license agreements.