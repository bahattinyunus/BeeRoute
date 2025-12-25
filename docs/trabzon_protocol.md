# The Trabzon Protocol 🏔️
> **Resilient. Fast. Unstoppable.**

## Overview
The **Trabzon Protocol** is the architectural backbone of BeeRoute. Inspired by the steep, rugged terrain of the Trabzon region and the tireless energy of its people, this protocol ensures that data packets (or logistical units) find their destination regardless of network obstacles.

## Core Principles

### 1. Hornet-Strike Latency
The protocol prioritizes speed above all else. Just as a hornet strikes without hesitation, the routing algorithm aggressively prunes suboptimal branches in the search tree.

### 2. The "Yaylalar" Topology (High-Altitude Routing)
Network nodes are hierarchically organized.
- **Valley Nodes**: High congestion, local traffic.
- **Plateau (Yayla) Nodes**: High-bandwidth, long-distance active links.
The algorithm prefers "climbing" to a Plateau Node for long-distance traversals, mimicking the local practice of using highland paths to bypass valley traffic.

## Mathematical Model

The probability $P_{ij}$ of a bee choosing passing from node $i$ to $j$ is given by:

$$ P_{ij} = \frac{\tau_{ij}^\alpha \cdot \eta_{ij}^\beta}{\sum_{k \in \text{allowed}} \tau_{ik}^\alpha \cdot \eta_{ik}^\beta} $$

Where:
- $\tau_{ij}$: Pheromone intensity (historical success)
- $\eta_{ij}$: Heuristic visibility ($1/d_{ij}$)
- $\alpha, \beta$: Control parameters (configured in `colony.yaml`)

## Failure Recovery: "Inat" Mode (Stubbornness)
If a route fails, the protocol enters **Inat Mode**. It does not back down; it brute-forces a local alternative path with increased pheromone deposition, signaling "We *will* get through here."

---
*Authored by Bahattin Yunus Çetin - IT Architect*
