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

- `agrofalcon.facturas`
- `agrofalcon.pedidos`

### SQS queues

- `new-leads`
- `orders`
- `invoices`

For the current `n8n` AWS S3 node, the dotted bucket names are the safest option to use with a custom LocalStack S3 endpoint:

- `agrofalcon.facturas`
- `agrofalcon.pedidos`

## Repository Structure

```text
compose.yaml
.env.example
localstack/
n8n/workflows/
odoo/addons/
README.md
```

## Custom Odoo Addon

The repository includes a starter addon:

- `odoo/addons/agrofalcon_crm`

It extends CRM leads with a few fields that are useful for this project:

- customer type
- crop interest
- expected order volume
- external event status
- S3 document key

To install it:

1. Restart Odoo after pulling changes.
2. Enable developer mode in Odoo.
3. Open `Apps`.
4. Click `Update Apps List`.
5. Search for `Agrofalcon CRM`.
6. Install the module.
