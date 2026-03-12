from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class MenuNode:
    key: str
    label: str
    children: Dict[str, "MenuNode"]


def default_menu() -> MenuNode:
    return MenuNode(
        key="root",
        label="Main Menu",
        children={
            "1": MenuNode(
                key="pm_kisan",
                label="PM-KISAN: benefits, eligibility, complaints",
                children={
                    "1": MenuNode(key="pm_kisan_benefits", label="Benefits", children={}),
                    "2": MenuNode(key="pm_kisan_eligibility", label="Eligibility check", children={}),
                    "3": MenuNode(key="pm_kisan_complaint", label="Complaint filing guidance", children={}),
                },
            ),
            "2": MenuNode(
                key="scholarships",
                label="Student scholarships",
                children={
                    "1": MenuNode(key="scholarships_find", label="Find suitable scholarships", children={}),
                    "2": MenuNode(key="scholarships_eligibility", label="Scholarship eligibility checklist", children={}),
                },
            ),
            "3": MenuNode(
                key="health_schemes",
                label="Health schemes",
                children={
                    "1": MenuNode(key="health_overview", label="Scheme overview", children={}),
                    "2": MenuNode(key="health_eligibility", label="Eligibility checklist", children={}),
                },
            ),
            "4": MenuNode(key="ai_agent", label="Ask Groq AI agent", children={}),
        },
    )


def render_menu(node: MenuNode) -> str:
    lines = [f"{node.label}:"]
    for k, child in node.children.items():
        lines.append(f"{k}) {child.label}")
    lines.append("Type the option number.")
    return "\n".join(lines)


def select_option(node: MenuNode, choice: str) -> Optional[MenuNode]:
    return node.children.get(choice.strip())
