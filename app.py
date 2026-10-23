import streamlit as st
import json
import os
import time
import uuid
from datetime import datetime
import pandas as pd

# -------------------------------------------------------------
# Page Configuration & UI Theme
# -------------------------------------------------------------
st.set_page_config(
    page_title="CloudKeep | Serverless Notes & NoSQL CRUD App",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for modern cloud notebook UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #78350f 0%, #b45309 50%, #d97706 100%);
        padding: 24px;
        border-radius: 14px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    }
    .main-header h1 {
        margin: 0;
        font-size: 26px;
        font-weight: 700;
        color: white !important;
    }
    .main-header p {
        margin-top: 6px;
        margin-bottom: 0;
        font-size: 14px;
        opacity: 0.95;
        color: #fef3c7;
    }
    
    .note-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 14px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .note-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    
    .tag-pill {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 9999px;
        font-size: 11px;
        font-weight: 600;
        margin-right: 6px;
    }
    .tag-devops { background: #e0f2fe; color: #0369a1; }
    .tag-cloud { background: #fef3c7; color: #92400e; }
    .tag-security { background: #fee2e2; color: #991b1b; }
    .tag-ai { background: #f3e8ff; color: #6b21a8; }
    .tag-general { background: #f1f5f9; color: #475569; }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Database Simulation (JSON File + Session State)
# -------------------------------------------------------------
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cloud_notes_database.json")

def seed_sample_notes():
    return [
        {
            "id": "note-001",
            "title": "AWS Lambda Serverless Best Practices",
            "category": "Cloud Architecture",
            "priority": "High",
            "content": "Key rules for building serverless microservices with AWS Lambda:\n- Keep handler functions stateless and lightweight.\n- Optimize cold starts by keeping package bundle size small.\n- Use environment variables and AWS Secrets Manager for credentials.\n- Configure appropriate memory allocation (CPU scales proportionally).",
            "created_at": "2026-10-23 09:00:00",
            "updated_at": "2026-10-23 09:15:00"
        },
        {
            "id": "note-002",
            "title": "NoSQL Document Stores vs Relational DBs",
            "category": "DevOps",
            "priority": "Medium",
            "content": "Comparison summary:\n- Relational (PostgreSQL, RDS): ACID compliant, rigid schema, complex JOINs, vertical scaling.\n- NoSQL (DynamoDB, MongoDB, Firestore): BASE model, flexible JSON documents, horizontal sharding, sub-10ms key-value lookups at scale.",
            "created_at": "2026-10-23 09:20:00",
            "updated_at": "2026-10-23 09:25:00"
        },
        {
            "id": "note-003",
            "title": "Cloud Security & IAM Least Privilege",
            "category": "Security",
            "priority": "High",
            "content": "Fundamental cloud security principle:\n- Never use the AWS root account for daily operations.\n- Grant minimal IAM permissions required for the task.\n- Enforce Multi-Factor Authentication (MFA) across all users.\n- Rotate API access keys every 90 days.",
            "created_at": "2026-10-23 09:30:00",
            "updated_at": "2026-10-23 09:30:00"
        }
    ]

def load_notes():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return seed_sample_notes()
    initial_notes = seed_sample_notes()
    save_notes(initial_notes)
    return initial_notes

def save_notes(notes):
    with open(DB_FILE, "w") as f:
        json.dump(notes, f, indent=2)

if "notes" not in st.session_state:
    st.session_state.notes = load_notes()
if "editing_note_id" not in st.session_state:
    st.session_state.editing_note_id = None

# -------------------------------------------------------------
# Header
# -------------------------------------------------------------
st.markdown("""
<div class="main-header">
    <h1>📝 CloudKeep — Serverless Notes & NoSQL CRUD App</h1>
    <p>Simulating serverless document storage (Amazon DynamoDB / Firebase Firestore) with auto-persistence and query filtering.</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# Sidebar: Cloud Concepts & Viva Guide
# -------------------------------------------------------------
with st.sidebar:
    st.subheader("🗄️ Simulated Cloud Database")
    st.caption("Engine: **Amazon DynamoDB / Firebase Firestore (Simulated)**")
    st.caption("Consistency Model: **Eventual Consistency / Strongly Consistent Read**")
    st.caption("Primary Key: `id` (Partition Key)")
    
    st.markdown("---")
    st.subheader("📥 Data Export & Backup")
    notes_json_str = json.dumps(st.session_state.notes, indent=2)
    st.download_button(
        label="💾 Download Database Backup (JSON)",
        data=notes_json_str,
        file_name="cloud_notes_backup.json",
        mime="application/json",
        use_container_width=True
    )
    
    st.markdown("---")
    with st.expander("🎓 College Viva Q&A Guide", expanded=False):
        st.markdown("""
**Q1: What is a Serverless Application?**
- A cloud execution model where the cloud provider dynamically manages server allocation, scaling, and patching. You only pay for exact compute milliseconds consumed (e.g. AWS Lambda + DynamoDB).

**Q2: What is Eventual Consistency in NoSQL?**
- When a document is updated, replicas across data centers may take milliseconds to sync. If you read immediately, you might receive the slightly older version before all nodes converge.

**Q3: Explain CRUD operations in Cloud APIs:**
- **Create:** HTTP `POST` or `PutItem` API
- **Read:** HTTP `GET` or `GetItem` / `Query` API
- **Update:** HTTP `PUT`/`PATCH` or `UpdateItem` API
- **Delete:** HTTP `DELETE` or `DeleteItem` API
        """)

# -------------------------------------------------------------
# Metrics Overview
# -------------------------------------------------------------
total_notes = len(st.session_state.notes)
all_words = sum(len(n.get("content", "").split()) for n in st.session_state.notes)
categories = list(set(n.get("category", "General") for n in st.session_state.notes))

col_m1, col_m2, col_m3, col_m4 = st.columns(4)
col_m1.metric("Total Saved Notes", f"{total_notes} documents")
col_m2.metric("Total Word Count", f"{all_words} words")
col_m3.metric("Active Categories", f"{len(categories)} tags")
col_m4.metric("Database Health", "Online", delta="Replica Synced")

st.markdown("<hr style='margin: 16px 0;'>", unsafe_allow_html=True)

# -------------------------------------------------------------
# Search & Filter Controls
# -------------------------------------------------------------
f_col1, f_col2, f_col3 = st.columns([2.5, 1.2, 1.2])

with f_col1:
    search_keyword = st.text_input("🔍 Search notes by title, content, or keyword...", placeholder="Type search term...")
with f_col2:
    filter_category = st.selectbox("Filter Category", ["All Categories"] + sorted(list(set(["Cloud Architecture", "DevOps", "Security", "AI & ML", "General"] + categories))))
with f_col3:
    filter_priority = st.selectbox("Filter Priority", ["All Priorities", "High", "Medium", "Low"])

# Filter logic
filtered_notes = st.session_state.notes
if search_keyword:
    kw = search_keyword.lower()
    filtered_notes = [n for n in filtered_notes if kw in n["title"].lower() or kw in n["content"].lower()]
if filter_category != "All Categories":
    filtered_notes = [n for n in filtered_notes if n.get("category") == filter_category]
if filter_priority != "All Priorities":
    filtered_notes = [n for n in filtered_notes if n.get("priority") == filter_priority]

# -------------------------------------------------------------
# Create or Edit Note Form
# -------------------------------------------------------------
with st.expander("➕ Create New Note / Document", expanded=st.session_state.editing_note_id is not None):
    # Check if in edit mode
    editing_item = None
    if st.session_state.editing_note_id:
        editing_item = next((n for n in st.session_state.notes if n["id"] == st.session_state.editing_note_id), None)
        st.info(f"✏️ Editing Document: **{editing_item['title']}** (ID: `{editing_item['id']}`)")
    
    with st.form("note_form", clear_on_submit=False):
        form_c1, form_c2, form_c3 = st.columns([2, 1, 1])
        with form_c1:
            form_title = st.text_input("Note Title", value=editing_item["title"] if editing_item else "", placeholder="e.g. Microservices Architecture Pattern")
        with form_c2:
            form_cat = st.selectbox(
                "Category Tag",
                ["Cloud Architecture", "DevOps", "Security", "AI & ML", "General"],
                index=["Cloud Architecture", "DevOps", "Security", "AI & ML", "General"].index(editing_item["category"]) if editing_item and editing_item["category"] in ["Cloud Architecture", "DevOps", "Security", "AI & ML", "General"] else 0
            )
        with form_c3:
            form_priority = st.selectbox(
                "Priority Level",
                ["High", "Medium", "Low"],
                index=["High", "Medium", "Low"].index(editing_item["priority"]) if editing_item and editing_item["priority"] in ["High", "Medium", "Low"] else 1
            )
            
        form_content = st.text_area("Note Content (Markdown supported)", value=editing_item["content"] if editing_item else "", height=150, placeholder="Write note details here...")
        
        btn_c1, btn_c2 = st.columns([1, 4])
        with btn_c1:
            submit_btn = st.form_submit_button("💾 Save Document", type="primary")
        with btn_c2:
            if editing_item:
                if st.form_submit_button("Cancel Edit"):
                    st.session_state.editing_note_id = None
                    st.rerun()

        if submit_btn:
            if not form_title.strip():
                st.error("Document Title cannot be blank.")
            else:
                now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if editing_item:
                    # Update
                    editing_item["title"] = form_title.strip()
                    editing_item["category"] = form_cat
                    editing_item["priority"] = form_priority
                    editing_item["content"] = form_content
                    editing_item["updated_at"] = now_str
                    st.session_state.editing_note_id = None
                    save_notes(st.session_state.notes)
                    st.success("Document updated successfully in simulated NoSQL database!")
                else:
                    # Create
                    new_doc = {
                        "id": f"note-{str(uuid.uuid4())[:8]}",
                        "title": form_title.strip(),
                        "category": form_cat,
                        "priority": form_priority,
                        "content": form_content,
                        "created_at": now_str,
                        "updated_at": now_str
                    }
                    st.session_state.notes.insert(0, new_doc)
                    save_notes(st.session_state.notes)
                    st.success("New document created and committed to storage!")
                time.sleep(0.5)
                st.rerun()

# -------------------------------------------------------------
# Notes Display Grid
# -------------------------------------------------------------
st.markdown(f"### 🗃️ Notes Repository ({len(filtered_notes)} notes)")

if not filtered_notes:
    st.info("No documents match your query.")
else:
    for note in filtered_notes:
        nid = note["id"]
        with st.container():
            col_main, col_ops = st.columns([5, 1.2])
            
            with col_main:
                cat = note.get("category", "General")
                cat_class = "tag-cloud" if "Cloud" in cat else ("tag-devops" if "DevOps" in cat else ("tag-security" if "Security" in cat else ("tag-ai" if "AI" in cat else "tag-general")))
                prio = note.get("priority", "Medium")
                prio_icon = "🔴" if prio == "High" else ("🟡" if prio == "Medium" else "🟢")
                
                st.markdown(f"#### {note['title']}")
                st.markdown(f"""
                <span class="tag-pill {cat_class}">{cat}</span>
                <span style="font-size: 12px; color: #64748b; font-weight: 500;">{prio_icon} {prio} Priority | ID: <code>{nid}</code> | Last Modified: {note.get('updated_at', note.get('created_at'))}</span>
                """, unsafe_allow_html=True)
                
                # Note Content
                st.markdown(note["content"])
                
            with col_ops:
                st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
                # Edit button
                if st.button("✏️ Edit", key=f"edit_{nid}", use_container_width=True):
                    st.session_state.editing_note_id = nid
                    st.rerun()
                    
                # Delete button
                if st.button("🗑️ Delete", key=f"del_{nid}", use_container_width=True):
                    st.session_state.notes = [n for n in st.session_state.notes if n["id"] != nid]
                    save_notes(st.session_state.notes)
                    st.toast(f"Deleted note: '{note['title']}'", icon="🗑️")
                    time.sleep(0.4)
                    st.rerun()

            st.markdown("<hr style='margin: 12px 0; border: 0.5px solid #f1f5f9;'>", unsafe_allow_html=True)
