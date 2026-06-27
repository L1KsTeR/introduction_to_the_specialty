# 🔒 Отчёт о безопасности зависимостей

## 📋 SBOM (Software Bill of Materials)

Сгенерирован через **Trivy** в формате CycloneDX (стандарт индустрии).

### Команда генерации:
```bash
trivy fs requirements.txt --format cyclonedx --output sbom.json
