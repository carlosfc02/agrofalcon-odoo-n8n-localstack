# Agrofalcon Local CRM

Personal learning project to explore `Odoo + CRM + n8n + LocalStack` with a realistic business scenario.

## Project Scenario

This project simulates a small agricultural company that:

- sells vegetables to shops and restaurants,
- captures leads in a CRM,
- converts opportunities into sales,
- manages product stock,
- issues invoices,
- and stores events/files in locally emulated AWS services.

## Tech Stack

- `Odoo` for CRM, sales, inventory, and invoicing
- `n8n` for workflow automation
- `LocalStack` for local AWS emulation
- `PostgreSQL` for persistence
- `Docker Compose` for local orchestration

## Current Goals

- create CRM opportunities in Odoo,
- automate lead processing with n8n,
- send events to `SQS`,
- store documents in `S3`,
- keep the full project reproducible from source control.

## Local Services

After startup, the project exposes:

- `Odoo`: `http://localhost:8069`
- `n8n`: `http://localhost:5678`
- `LocalStack`: `http://localhost:4566`

## LocalStack Resources

The initialization script creates:

### S3 buckets

- `agrofalcon-facturas`
- `agrofalcon-pedidos`

### SQS queues

- `new-leads`
- `orders`
- `invoices`

## Repository Structure

```text
compose.yaml
.env.example
localstack/
n8n/workflows/
odoo/addons/
README.md
```


