# UrjaSahayak AI

> AI-powered energy supply-chain resilience platform for geopolitical risk monitoring, disruption simulation, procurement rerouting, and strategic petroleum reserve planning.

## Problem Statement

India is highly dependent on imported crude oil. Disruptions caused by geopolitical tensions, sanctions, maritime attacks, port closures, or shipping-route blockages can delay crude supply, increase freight and insurance costs, affect refinery operations, and put pressure on strategic petroleum reserves.

UrjaSahayak AI helps decision-makers understand these risks and generate faster, data-driven supply-chain response plans.

## Our Solution

UrjaSahayak AI is an explainable AI decision-support platform that:

- Monitors geopolitical and logistics risk signals
- Generates corridor-level and supplier-level disruption risk scores
- Simulates supply-chain disruption scenarios
- Estimates supply shortages, delays, and additional procurement costs
- Recommends alternative crude suppliers and shipping routes
- Suggests strategic petroleum reserve drawdown schedules
- Visualizes supply routes, chokepoints, ports, and refineries on an interactive map

## Core Features

### 1. Geopolitical Risk Intelligence

Analyzes geopolitical, sanctions, shipping, and logistics events to estimate disruption risk for key maritime corridors and crude-oil suppliers.

Example:

```text
Corridor: Strait of Hormuz
Risk score: 78/100
Disruption probability: 72%
Expected duration: 14 days
```

### 2. Disruption Scenario Simulator

Simulates events such as:

- Strait of Hormuz closure
- Red Sea shipping suspension
- Supplier sanctions
- Port outage
- Freight-cost increase
- Insurance-cost increase

The simulator estimates crude supply shortfall, route delays, procurement cost impact, and reserve requirements.

### 3. Adaptive Procurement Orchestrator

Ranks alternative procurement options using:

- Supplier availability
- Route risk
- Transit time
- Freight cost
- Insurance cost
- Port capacity
- Refinery compatibility
- Sanctions exposure

### 4. Strategic Reserve Optimisation

Recommends an optimal strategic petroleum reserve drawdown plan based on expected supply gaps, incoming cargoes, and a configurable reserve safety threshold.

### 5. Energy Supply Chain Digital Twin

Provides an interactive geospatial view of:

- Crude-oil suppliers
- Shipping corridors
- Maritime chokepoints
- Indian ports
- Refineries
- Strategic reserve locations
- Disrupted and alternate routes

## System Workflow

```text
Geopolitical / Shipping / Sanctions Events
                  ↓
       Risk Intelligence Engine
                  ↓
   Corridor and Supplier Risk Scores
                  ↓
       Disruption Scenario Simulator
                  ↓
 Supply Shortfall and Cost Impact Estimate
                  ↓
    Procurement Route Optimization Engine
                  ↓
 Alternative Supplier and Route Recommendation
                  ↓
 Strategic Petroleum Reserve Drawdown Plan
```

## Technology Stack

| Component | Planned Technology |
|---|---|
| Frontend | React, Vite, Tailwind CSS |
| Maps | Leaflet or MapLibre |
| Charts | Recharts |
| Backend | Python, FastAPI |
| Data Processing | Pandas, NumPy |
| Optimization | OR-Tools / SciPy |
| Database | SQLite for prototype, PostgreSQL for scale |
| AI / NLP | Structured event extraction and risk classification |
| Deployment | Vercel + Render / Railway |

## Repository Structure

```text
UrjaSahayak-AI/
├── frontend/           # React dashboard
├── backend/            # FastAPI APIs, AI/risk engine, simulation and optimization
├── data/               # Sample suppliers, routes, ports and risk-event datasets
├── docs/               # Architecture, assumptions and screenshots
├── demo/               # Demo-video link and submission material
├── .gitignore
└── README.md
```

## Current Development Status

The project is currently in the prototype-development stage.

Planned first prototype flow:

1. Select a disruption scenario, such as a 14-day Strait of Hormuz closure.
2. Calculate expected supply shortage and disruption cost.
3. Visualize blocked shipping routes and affected suppliers.
4. Rank alternative suppliers and routes.
5. Recommend a strategic reserve drawdown schedule.
6. Display an explainable response plan.

## Local Setup

The setup instructions will be updated as development progresses.

### Planned requirements

- Node.js 18 or newer
- Python 3.10 or newer
- Git

### Planned startup commands

```bash
git clone https://github.com/BRILLIANT005/UrjaSahayak-AI.git
cd UrjaSahayak-AI
```

## Data and Assumptions

This hackathon prototype will use a combination of public and simulated data.

Some values—such as supplier availability, route capacity, refinery compatibility, disruption duration, freight cost, and economic impact—will be simplified for prototype demonstration. The tool provides decision support and does not autonomously execute procurement actions.

## Future Scope

- Real-time news and sanctions feeds
- AIS vessel tracking and maritime alerts
- Live crude-price and freight-rate feeds
- Advanced refinery crude-compatibility modelling
- LNG, coal, and critical-mineral supply-chain support
- Automated alert notifications
- Multi-agency response coordination

## Team

| Name | Role |
|---|---|
| Barkha Alok Gupta | Full-stack development / AI integration |
| Barkha Alok Gupta | Frontend / UI-UX |
| Swanandi Bhadade | Backend / data modelling |
| Swanandi Bhadade | Research / testing / presentation |

## Demo Video

Demo video link will be added before final submission.

## Live Prototype

Live prototype link will be added before final submission.

## License

Created for hackathon submission.
