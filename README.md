> ⚠️ This repository contains the **final frozen MVP** for hackathon submission.
# Disaster Alert System with Alert Fatigue Control (MVP)

## Problem Statement
**PS-6: Disaster Alert System with Alert Fatigue Control**

In many emergency systems, users receive frequent alerts, including low-severity or repetitive notifications. Over time, this leads to **alert fatigue**, where users start ignoring alerts, disable notifications, or respond late during real emergencies. This can result in serious safety risks during disasters.

---

## What is Alert Fatigue?
Alert fatigue occurs when users are exposed to too many alerts in a short period of time. Even important warnings may be ignored if users lose trust in the alerting system. Preventing alert fatigue while still ensuring public safety is a critical challenge in disaster management systems.

---

## Solution Overview
This project presents a **software-based Minimum Viable Product (MVP)** that intelligently decides whether a disaster alert should be:

- **SEND** immediately  
- **DELAY** until a later time  
- **SUPPRESS** to avoid unnecessary notifications  

The decision is made by balancing:
- Disaster risk
- User alert fatigue

The system also provides a **clear explanation** for every decision, ensuring transparency and trust.

---

## System Approach

### Inputs
- Disaster severity (Low / Medium / High)
- Area risk level (Low / Medium / High)
- Time since last alert (in hours)

### Core Logic
1. A **Risk Score** is calculated based on disaster severity and area risk.
2. A **Fatigue Level** is calculated based on how recently alerts were sent.
3. A rule-based decision engine determines whether to SEND, DELAY, or SUPPRESS the alert.
4. An explanation is generated to justify the decision.

---

## Decision Logic (Explainable AI)

- High risk + Low fatigue → **SEND**
- Medium risk + High fatigue → **DELAY**
- Low risk + High fatigue → **SUPPRESS**

This rule-based approach ensures that decisions are **transparent, interpretable, and explainable**.

---

## Technology Used
- Python
- Rule-based decision logic
- GitHub

---

## How to Run the MVP
1. Download `mvp.py`
2. Open Command Prompt / Terminal
3. Navigate to the file location
4. Run:
   ```bash
   python mvp.py
