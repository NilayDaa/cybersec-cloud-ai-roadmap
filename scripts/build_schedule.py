#!/usr/bin/env python3
"""Generate schedule.json — 72 daily study tasks (12 weeks x 6 days)."""
import json

# Each week: (week_name, [day1..day6]) where each day is:
#   (title, [tasks...], [resource_links...], [project_flag...])
PLAN = [
    # ---- WEEK 1: Cyber Fundamentals ----
    ("W1 Cyber Fundamentals", [
        ("Linux + Windows fundamentals", [
            "THM Cyber Security 101: Linux modules",
            "Recap: file system, permissions, users, processes",
            "Recreate: basic bash (find, grep, awk, curl, tar, ssh)",
            "Windows: filesystem, registry, users, cmd & PowerShell basics",
        ], ["https://tryhackme.com/path/outline/cybersecurity101", "https://tryhackme.com/path/outline/presecurity"]),
        ("Networking + TCP/IP recap", [
            "THM networking: OSI, TCP/IP, ports, subnets",
            "Recap: TCP handshake, UDP, DNS, DHCP, HTTP(S)",
            "20 subnetting exercises",
        ], ["https://www.netacad.com/", "https://subnettingpractice.com/"]),
        ("Active Directory fundamentals", [
            "AD concepts: domains, forests, group policy, Kerberos",
            "THM Active Directory module",
            "Practical: enumerate a small AD lab",
        ], ["https://tryhackme.com/path/outline/cybersecurity101"]),
        ("Cryptography + web security", [
            "Crypto: hashing, symmetric/asymmetric, TLS",
            "OWASP Top 10 overview",
            "SQL security: injection basics",
            "Web security: auth, sessions, CSRF, XSS",
        ], ["https://owasp.org/www-project-top-ten/", "https://portswigger.net/web-security"]),
        ("Tooling drill: recon + scanning", [
            "Nmap: host/port/service/version/script scanning",
            "Wireshark + tcpdump: capture & analyze",
            "Netcat: connect, listen, file transfer",
            "Gobuster: dir/wordlist enumeration",
        ], ["https://tryhackme.com/path/outline/cybersecurity101"]),
        ("Web attack tools", [
            "Burp Suite: proxy, repeater, intruder",
            "Hydra: brute force practice",
            "Metasploit: basics, msfconsole, aux modules",
            "Vuln scanning + IDS/firewall concepts",
        ], ["https://portswigger.net/web-security", "https://tryhackme.com/"]),
    ]),

    # ---- WEEK 2: SOC ----
    ("W2 SOC", [
        ("SOC fundamentals", [
            "THM SOC Level 1: security operations intro",
            "SOC roles, process, alert triage",
        ], ["https://tryhackme.com/path/outline/soclevel1"]),
        ("Log analysis + SIEM", [
            "Log formats: syslog, Windows event logs, web logs",
            "Set up Wazuh lab",
            "SIEM querying & alert investigations",
        ], ["https://tryhackme.com/path/outline/soclevel1"]),
        ("Threat detection + incident response", [
            "Detection engineering basics",
            "Incident response lifecycle",
            "Digital forensics essentials",
        ], ["https://attack.mitre.org/", "https://tryhackme.com/path/outline/soclevel1"]),
        ("SOC investigation practice 1", [
            "Investigate 2 alerts end-to-end on Wazuh",
            "Write investigation #1 (triage->detection->containment)",
        ], ["https://tryhackme.com/path/outline/soclevel1"]),
        ("SOC investigation practice 2", [
            "Investigate 2 more alerts",
            "Write investigations #2 & #3",
        ], ["https://tryhackme.com/path/outline/soclevel1"]),
        ("SOC wrap-up", [
            "Complete remaining SOC Level 1 modules",
            "Write investigations #4 & #5",
            "Document all 5 investigations in docs/",
        ], ["https://tryhackme.com/path/outline/soclevel1"]),
    ]),

    # ---- WEEK 3: Penetration Testing ----
    ("W3 Pentest", [
        ("Recon + enumeration", [
            "THM Jr Penetration Tester: recon",
            "Active + passive recon, OSINT",
        ], ["https://tryhackme.com/path/outline/jrpenetrationtester"]),
        ("Web exploitation", [
            "THM web exploitation modules",
            "PortSwigger labs: SQLi, XSS, SSRF, file upload",
        ], ["https://portswigger.net/web-security", "https://tryhackme.com/path/outline/jrpenetrationtester"]),
        ("Privilege escalation", [
            "Linux privesc: SUID, sudo, cron, kernel",
            "Windows privesc basics",
        ], ["https://tryhackme.com/path/outline/jrpenetrationtester"]),
        ("Post-exploitation + pivoting", [
            "Meterpreter sessions, lateral movement",
            "Basic pivoting",
        ], ["https://tryhackme.com/path/outline/jrpenetrationtester"]),
        ("CTF day 1-2", [
            "Solve 3 legal CTF/lab machines",
            "Log methodology + commands",
        ], ["https://tryhackme.com/", "https://academy.hackthebox.com/"]),
        ("CTF day 3 + reporting", [
            "Solve 2 more machines",
            "Write a full penetration-test report",
        ], ["https://academy.hackthebox.com/"]),
    ]),

    # ---- WEEK 4: Azure Fundamentals ----
    ("W4 Azure Fundamentals", [
        ("Cloud concepts", [
            "MS path: Describe cloud concepts",
            "IaaS/PaaS/SaaS, public/private/hybrid, regions, AZ",
        ], ["https://learn.microsoft.com/en-us/training/paths/microsoft-azure-fundamentals-describe-cloud-concepts/"]),
        ("Azure architecture & services 1", [
            "MS path: arch + services (compute, storage)",
            "Azure VMs, storage accounts",
        ], ["https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/"]),
        ("Azure architecture & services 2", [
            "Networking: VNet, LB, DNS",
            "Containers: ACI, AKS",
            "Databases: SQL, Cosmos DB",
        ], ["https://learn.microsoft.com/en-us/training/paths/azure-fundamentals-describe-azure-architecture-services/"]),
        ("Management & governance", [
            "MS path: management & governance",
            "RBAC, IAM, policies, resource groups, monitoring, cost",
        ], ["https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/"]),
        ("AZ-900 decision + practice", [
            "Decide: take AZ-900?",
            "If yes: MS Learn AZ-900 path + practice tests",
            "Free Azure account setup",
        ], ["https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/", "https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-900"]),
        ("Azure hands-on", [
            "Build free-tier resources in portal",
            "Create a VM, storage, and a simple VNet",
        ], ["https://learn.microsoft.com/en-us/training/azure/"]),
    ]),

    # ---- WEEK 5: Docker + K8s ----
    ("W5 Docker + K8s", [
        ("Docker fundamentals", [
            "Docker Get Started: images, containers, Dockerfile, ports, volumes, networks",
            "Healthcheck, non-root, multi-stage",
        ], ["https://docs.docker.com/get-started/"]),
        ("Docker Compose", [
            "Compose for multi-container apps",
            "Registries + image tagging",
            "Container security basics",
        ], ["https://docs.docker.com/get-started/"]),
        ("Containerize the stack", [
            "Containerize FastAPI backend",
            "Containerize React frontend",
            "Add PostgreSQL + Redis containers",
            "Full Docker Compose app running",
        ], ["https://docs.docker.com/get-started/"]),
        ("K8s fundamentals", [
            "K8s tutorial: architecture, clusters, nodes, Pods, Deployments, Services",
            "kubectl basics",
        ], ["https://kubernetes.io/docs/tutorials/"]),
        ("K8s config + storage", [
            "Ingress, Namespaces, ConfigMaps, Secrets",
            "PV/PVC, StatefulSets",
        ], ["https://kubernetes.io/docs/tutorials/"]),
        ("K8s security + deploy", [
            "RBAC, NetworkPolicies, resource limits, HPA",
            "Deploy FastAPI+Postgres+Redis to K8s with full config",
        ], ["https://kubernetes.io/docs/tutorials/"]),
    ]),

    # ---- WEEK 6: ML + LLM ----
    ("W6 ML + LLM", [
        ("ML fundamentals", [
            "Google ML Crash Course (accelerated, deep-dive only where unsure)",
            "regression, classification, features, labels, overfitting",
        ], ["https://developers.google.com/machine-learning/crash-course"]),
        ("ML build day", [
            "Build compact regression + classification projects",
            "Build a neural-network project",
        ], ["https://developers.google.com/machine-learning/crash-course"]),
        ("LLM: transformers + tokenization", [
            "HF LLM Course: Transformers, tokenization, attention, embeddings",
        ], ["https://huggingface.co/learn/llm-course/"]),
        ("LLM: inference + fine-tuning", [
            "HF: inference, fine-tuning, eval",
            "Run a local open-source LLM",
        ], ["https://huggingface.co/learn/llm-course/"]),
        ("Embeddings + LLM API", [
            "Build an embedding-search project",
            "Build an LLM API with FastAPI",
        ], ["https://huggingface.co/learn/llm-course/"]),
        ("Model eval + wrap", [
            "Model evaluation, validation, test sets",
            "Push one ML/LLM project to GitHub",
        ], ["https://huggingface.co/learn/llm-course/"]),
    ]),

    # ---- WEEK 7: RAG (Portfolio Project 3) ----
    ("W7 RAG", [
        ("RAG architecture", [
            "Document ingestion, PDF processing, chunking",
            "Embeddings + vector DBs + similarity search + retrieval",
        ], ["https://huggingface.co/learn/llm-course/"]),
        ("Vector stores", [
            "FAISS + PostgreSQL pgvector",
            "RAG evaluation",
        ], ["https://github.com/pgvector/pgvector", "https://github.com/facebookresearch/faiss"]),
        ("Build RAG scaffold", [
            "FastAPI app + document upload + ingestion pipeline",
        ], ["https://huggingface.co/learn/llm-course/"]),
        ("RAG hardening (security)", [
            "Auth, RBAC, rate limiting, logging",
            "Prompt injection + context injection",
        ], ["https://genai.owasp.org/initiative/owasp-top-10-for-llm-and-genai/"]),
        ("RAG testing", [
            "Test against wrong answers + prompt injection",
            "Document evaluation results",
        ], ["https://genai.owasp.org/"]),
        ("Deploy RAG", [
            "Deploy securely with Docker",
            "Write security documentation + README",
        ], ["https://github.com/NilayDaa/ai-job-agent"]),
    ]),

    # ---- WEEK 8: AI Agents (flagship upgrade) ----
    ("W8 AI Agents", [
        ("Agent fundamentals", [
            "HF Agents Course: agent loops, tools, tool/function calling, reasoning, planning",
            "smolagents, LangGraph, LlamaIndex",
        ], ["https://huggingface.co/learn/agents-course/"]),
        ("Agentic patterns", [
            "Agentic RAG, agent evaluation, GAIA",
        ], ["https://huggingface.co/learn/agents-course/"]),
        ("Build agents", [
            "Simple tool-calling agent",
            "Research agent",
            "RAG agent",
            "Multi-tool agent",
        ], ["https://huggingface.co/learn/agents-course/"]),
        ("Upgrade AI Job Agent: tools", [
            "Add tool-calling to AI Job Agent",
            "Wire LangGraph",
        ], ["https://github.com/NilayDaa/ai-job-agent"]),
        ("Upgrade AI Job Agent: eval + docs", [
            "Add agent evaluation",
            "Document architecture",
            "Push to GitHub",
        ], ["https://github.com/NilayDaa/ai-job-agent"]),
        ("Agent security", [
            "LLM-gen AI frameworks: excessive agency, tool abuse, agent hijacking",
            "Review OWASP LLM Top 10 relevant to agents",
        ], ["https://genai.owasp.org/initiative/owasp-top-10-for-llm-and-genai/"]),
    ]),

    # ---- WEEK 9: DevSecOps + Azure Security ----
    ("W9 DevSecOps + Azure Security", [
        ("CI/CD + GitHub Actions", [
            "GitHub Skills: Actions, CI/CD, automation",
            "Git + GitHub workflow recap",
        ], ["https://skills.github.com/"]),
        ("SAST + secret + dependency scanning", [
            "Semgrep: add SAST to a project",
            "Gitleaks: secret scanning",
            "Dependency scanning on a project",
        ], ["https://semgrep.dev/", "https://github.com/gitleaks/gitleaks"]),
        ("Container + DAST scanning", [
            "Trivy container scanning",
            "OWASP ZAP DAST",
        ], ["https://trivy.dev/", "https://www.zaproxy.org/"]),
        ("Fail-closed CI", [
            "Make security failures stop CI/CD deployment",
            "Wire all scanners into one pipeline",
        ], ["https://skills.github.com/"]),
        ("Azure security core", [
            "Entra ID, IAM, RBAC, NSG, Azure Firewall, Key Vault",
            "Defender for Cloud, Monitor, logging",
        ], ["https://tryhackme.com/path/outline/azuresecurity", "https://learn.microsoft.com/en-us/security/zero-trust/"]),
        ("Zero Trust + securing my Azure stack", [
            "Zero Trust architecture",
            "Apply NSG + Key Vault + logging to my AZ resource group",
        ], ["https://learn.microsoft.com/en-us/security/zero-trust/"]),
    ]),

    # ---- WEEK 10: AI Security + Sentinel ----
    ("W10 AI Security", [
        ("AI Security fundamentals", [
            "Microsoft AI Security Fundamentals path",
        ], ["https://learn.microsoft.com/en-us/training/paths/ai-security-fundamentals/"]),
        ("OWASP LLM Top 10", [
            "OWASP Top 10 for LLM apps: each entry + mitigation",
        ], ["https://genai.owasp.org/initiative/owasp-top-10-for-llm-and-genai/"]),
        ("Attack classes", [
            "Prompt injection, indirect injection, jailbreaking, prompt-defense",
            "RAG poisoning, data poisoning, sensitive-info disclosure",
        ], ["https://genai.owasp.org/initiative/owasp-top-10-for-llm-and-genai/"]),
        ("Agent attack classes", [
            "Excessive agency, tool abuse, agent hijacking, AI supply chain",
            "AI threat modelling + red teaming principles",
        ], ["https://genai.owasp.org/initiative/owasp-top-10-for-llm-and-genai/"]),
        ("THM AI Security + Defending Azure", [
            "THM AI Security path",
            "THM Defending Azure: Sentinel, KQL, Defender XDR, detection, investigation",
        ], ["https://tryhackme.com/path/outline/aisecurity", "https://tryhackme.com/path/outline/azuresecurity", "https://learn.microsoft.com/en-us/azure/sentinel/"]),
        ("Sentinel hands-on", [
            "Spin up Sentinel log analytics workspace",
            "Write KQL queries, create simple detection rule",
        ], ["https://learn.microsoft.com/en-us/azure/sentinel/"]),
    ]),

    # ---- WEEK 11: Projects (flagship: AI SOC Analyst) ----
    ("W11 Projects", [
        ("AI SOC Analyst: ingestion + SIEM", [
            "Build security-log ingestion pipeline",
            "Connect Wazuh/Sentinel data source",
            "Alert-processing pipeline",
        ], ["https://attack.mitre.org/", "https://github.com/NilayDaa/ai-job-agent"]),
        ("AI SOC Analyst: agent + RAG", [
            "Build AI SOC agent",
            "Add security-knowledge RAG",
            "MITRE ATT&CK mapping",
        ], ["https://attack.mitre.org/", "https://huggingface.co/learn/agents-course/"]),
        ("AI SOC Analyst: investigation + guardrails", [
            "Investigation tools + threat analysis",
            "Generate incident reports",
            "Human-approval before actions + audit trail",
        ], ["https://github.com/NilayDaa/ai-job-agent"]),
        ("AI SOC Analyst: eval + deploy", [
            "Add evaluation dataset",
            "Deploy the app",
            "Write security report",
        ], ["https://github.com/NilayDaa/ai-job-agent"]),
        ("AI Security Lab: build vulnerable app", [
            "Intentionally vulnerable GenAI app",
            "Demonstrate prompt injection, indirect injection, jailbreaking",
        ], ["https://genai.owasp.org/initiative/owasp-top-10-for-llm-and-genai/"]),
        ("AI Security Lab: attacks + defenses", [
            "Demonstrate RAG poisoning, data leakage, tool abuse, excessive agency",
            "Implement defenses, retest",
            "Write security report + publish sanitized",
        ], ["https://genai.owasp.org/initiative/owasp-top-10-for-llm-and-genai/"]),
    ]),

    # ---- WEEK 12: HTB + Launch ----
    ("W12 Launch", [
        ("HTB Academy reset", [
            "Pick SOC + Web security track",
            "Complete 1-2 advanced HTB machines",
            "Document every major lab",
        ], ["https://academy.hackthebox.com/"]),
        ("HTB hands-on", [
            "Complete more HTB machines",
            "Red-team exercise write-up",
        ], ["https://academy.hackthebox.com/"]),
        ("Portfolio polish", [
            "READMEs, architecture diagrams, security docs on ALL projects",
            "Ensure 5 projects are on GitHub",
        ], ["https://github.com/NilayDaa/ai-job-agent"]),
        ("CV + LinkedIn", [
            "Update CV to lead with AI Job Agent + AI SOC Analyst",
            "Update LinkedIn headline + About (Finland internship framing)",
        ], ["https://github.com/NilayDaa/ai-job-agent"]),
        ("Interview prep", [
            "Compile technical interview questions (security + AI + cloud)",
            "Practice answering out loud",
        ], []),
        ("Launch", [
            "Start applying for internships + thesis positions",
            "Review roadmap, choose specialization",
            "Plan next cycle of deep work",
        ], []),
    ]),
]

# Build schedule
schedule = []
day_count = 0
for week_name, days in PLAN:
    for d in days:
        day_count += 1
        title, tasks, links = d
        schedule.append({
            "day": day_count,
            "week": week_name,
            "title": f"[Day {day_count}] {week_name} — {title}",
            "body": {
                "week": week_name,
                "topic": title,
                "tasks": tasks,
                "resources": links,
            },
        })

with open("schedule.json", "w") as f:
    json.dump({"total_days": day_count, "days": schedule}, f, indent=2)
print(f"Wrote {day_count} daily tasks to schedule.json")