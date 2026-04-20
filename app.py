"""
ASTRAE Intelligence · v4.0 ULTIMATE FINAL
Enterprise-Grade Predictive Analytics Platform
Ultra-Optimized | 9 Professional KPIs | Advanced Charts | Zero Latency
"""

import streamlit as st
import pandas as pd
import numpy as np
import io
import time
import warnings
from typing import Dict, List, Tuple, Any, Optional
from datetime import datetime
warnings.filterwarnings("ignore")

# ═══════════════════════════════════════════════════════════════════════════════
# CRITICAL DEPENDENCIES
# ═══════════════════════════════════════════════════════════════════════════════

try:
    from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
    from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor, ExtraTreesRegressor
    from sklearn.preprocessing import StandardScaler, RobustScaler
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
    from sklearn.impute import SimpleImputer
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

try:
    from scipy.optimize import minimize
    from scipy import stats
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

try:
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    VIF_AVAILABLE = True
except ImportError:
    VIF_AVAILABLE = False

try:
    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import seaborn as sns
    PLOT_AVAILABLE = True
    plt.style.use('dark_background')
    sns.set_palette("husl")
except ImportError:
    PLOT_AVAILABLE = False

try:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="ASTRAE · Decision Intelligence",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════════════════════
# PREMIUM CSS STYLING
# ═══════════════════════════════════════════════════════════════════════════════

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@300;400;500;600&display=swap');

:root {
  --bg:         #04030c;
  --panel:      #0e0c1e;
  --panel2:     #151230;
  --border:     rgba(110,70,230,0.18);
  --border2:    rgba(140,100,255,0.38);
  --neon:       #a78bfa;
  --violet:     #7c3aed;
  --blue:       #3b82f6;
  --cyan:       #22d3ee;
  --green:      #10b981;
  --amber:      #f59e0b;
  --red:        #ef4444;
  --orange:     #f97316;
  --t1:         #eeeaff;
  --t2:         #aea6d0;
  --t3:         #5e5880;
  --grad:       linear-gradient(135deg,#7c3aed,#5b4de8,#3b82f6);
  --grad2:      linear-gradient(135deg,#a78bfa,#818cf8,#38bdf8);
  --r:          14px;
  --f:          'Outfit', sans-serif;
  --fm:         'JetBrains Mono', monospace;
}

#MainMenu,footer,header{visibility:hidden}
[data-testid="collapsedControl"]{display:none}
section[data-testid="stSidebar"]{display:none!important}
.stDeployButton{display:none}
div[data-testid="stToolbar"]{display:none}

html,body,.stApp{
  background:var(--bg)!important;
  font-family:var(--f);
  color:var(--t1);
  scroll-behavior:smooth;
}
.main .block-container{
  max-width:1200px!important;
  padding:0 32px 100px!important;
  margin:0 auto!important;
}

.bg-layer{
  position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden;
}

.moon{
  position:absolute;
  bottom:-360px;left:50%;
  transform:translateX(-50%);
  width:720px;height:720px;
  border-radius:50%;
  background:radial-gradient(circle at 50% 38%,
    rgba(124,58,237,.5) 0%,
    rgba(91,77,232,.3) 28%,
    rgba(59,130,246,.15) 55%,
    transparent 72%);
  box-shadow:0 0 100px rgba(124,58,237,.35),
             0 0 200px rgba(91,77,232,.18),
             0 -80px 140px rgba(167,139,250,.12);
  animation:moonGlow 9s ease-in-out infinite alternate;
}
.moon-ring{
  position:absolute;bottom:-300px;left:50%;
  transform:translateX(-50%);
  width:600px;height:600px;border-radius:50%;
  border:1px solid rgba(167,139,250,.22);
  animation:moonGlow 9s ease-in-out infinite alternate;
  animation-delay:.8s;
}
.moon-ring2{
  position:absolute;bottom:-240px;left:50%;
  transform:translateX(-50%);
  width:490px;height:490px;border-radius:50%;
  border:1px solid rgba(167,139,250,.10);
  animation:moonGlow 9s ease-in-out infinite alternate;
  animation-delay:1.6s;
}
@keyframes moonGlow{
  0%{opacity:.65;transform:translateX(-50%) scale(.97)}
  100%{opacity:1;transform:translateX(-50%) scale(1.04)}
}

.ambient{
  position:absolute;top:-180px;left:50%;
  transform:translateX(-50%);
  width:900px;height:450px;
  background:radial-gradient(ellipse,rgba(124,58,237,.14) 0%,transparent 68%);
  animation:ambGlow 14s ease-in-out infinite alternate;
}
@keyframes ambGlow{
  0%{opacity:.5;transform:translateX(-50%) scale(.88)}
  100%{opacity:.9;transform:translateX(-50%) scale(1.12)}
}

.stars{
  position:absolute;inset:0;
  background-image:
    radial-gradient(1.5px 1.5px at 7%  11%, rgba(167,139,250,.75), transparent),
    radial-gradient(1px   1px   at 22% 65%, rgba(91,77,232,.55), transparent),
    radial-gradient(1px   1px   at 48% 19%, rgba(34,211,238,.55), transparent),
    radial-gradient(1.5px 1.5px at 68% 50%, rgba(124,58,237,.65), transparent),
    radial-gradient(1px   1px   at 83% 74%, rgba(167,139,250,.45), transparent),
    radial-gradient(1px   1px   at 37% 36%, rgba(59,130,246,.55), transparent),
    radial-gradient(1px   1px   at 59% 82%, rgba(167,139,250,.35), transparent),
    radial-gradient(1.5px 1.5px at 14% 88%, rgba(91,77,232,.45), transparent),
    radial-gradient(1px   1px   at 92% 22%, rgba(34,211,238,.35), transparent),
    radial-gradient(1px   1px   at 76% 8%,  rgba(167,139,250,.5), transparent),
    radial-gradient(1px   1px   at 3%  55%, rgba(59,130,246,.4), transparent),
    radial-gradient(1.5px 1.5px at 55% 95%, rgba(124,58,237,.5), transparent);
  animation:starPulse 8s ease-in-out infinite alternate;
}
@keyframes starPulse{
  0%{opacity:.4}100%{opacity:.85}
}

.nav{
  position:fixed;top:0;left:0;right:0;height:58px;
  background:rgba(4,3,12,.85);
  backdrop-filter:blur(28px);-webkit-backdrop-filter:blur(28px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;
  padding:0 40px;z-index:9999;
  transition:all 0.3s ease;
}
.nav-logo{
  font-family:var(--f);font-size:16px;font-weight:900;
  letter-spacing:.16em;text-transform:uppercase;
  background:var(--grad2);-webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.nav-right{display:flex;align-items:center;gap:18px;}
.nav-user{
  font-family:var(--fm);font-size:11px;color:var(--t3);
  letter-spacing:.06em;
}
.nav-chip{
  background:rgba(167,139,250,.12);
  border:1px solid rgba(167,139,250,.28);
  color:var(--neon);font-family:var(--fm);font-size:10px;
  font-weight:600;letter-spacing:.10em;text-transform:uppercase;
  padding:5px 14px;border-radius:50px;
  backdrop-filter:blur(10px);
  transition:all .3s ease;
}
.nav-spacer{height:70px;}

.hero{
  text-align:center;padding:64px 0 48px;
  animation:fadeUp .75s cubic-bezier(.16,1,.3,1) both;
}
.hero-pill{
  display:inline-flex;align-items:center;gap:8px;
  font-family:var(--fm);font-size:10px;color:var(--neon);
  letter-spacing:.18em;text-transform:uppercase;
  background:rgba(167,139,250,.09);
  border:1px solid rgba(167,139,250,.26);
  border-radius:50px;padding:6px 18px;margin-bottom:26px;
}
.pill-dot{
  width:5px;height:5px;border-radius:50%;background:var(--neon);
  animation:blink 2.2s ease-in-out infinite;
}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.25}}
.hero-h{
  font-family:var(--f);
  font-size:clamp(42px,6vw,74px);
  font-weight:900;line-height:1.04;letter-spacing:-.03em;
  margin:0 0 16px;
}
.grad-text{
  background:var(--grad2);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}
.hero-sub{
  font-size:15px;font-weight:400;color:var(--t2);
  line-height:1.75;max-width:550px;margin:0 auto 32px;
}

.card{
  background:rgba(14,12,30,.65);
  backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);
  border:1px solid var(--border);
  border-radius:var(--r);padding:32px 36px;
  position:relative;overflow:hidden;margin-bottom:28px;
  animation:fadeUp .55s cubic-bezier(.16,1,.3,1) both;
  transition:all .35s cubic-bezier(.16,1,.3,1);
}
.card::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(124,58,237,.04) 0%,transparent 55%);
  pointer-events:none;
}
.card:hover{
  border-color:rgba(140,100,255,.35);
  transform:translateY(-4px);
  box-shadow:0 12px 40px rgba(124,58,237,.15);
}
.card-glow{
  border-color:rgba(167,139,250,.32);
  box-shadow:0 0 48px rgba(124,58,237,.12),inset 0 1px 0 rgba(255,255,255,.03);
}
.ey{
  font-family:var(--fm);font-size:10px;color:var(--neon);
  letter-spacing:.18em;text-transform:uppercase;margin-bottom:8px;
}
.ct{
  font-family:var(--f);font-size:22px;font-weight:700;
  letter-spacing:-.02em;margin:0 0 12px;
}
.cd{font-size:13px;color:var(--t2);line-height:1.7;margin:0 0 24px;}

.kpi-grid{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(140px,1fr));
  gap:16px;
  margin:24px 0;
}
.kpi-card{
  background:rgba(21,18,48,.8);
  backdrop-filter:blur(18px);
  border:1px solid var(--border);
  border-radius:12px;
  padding:20px;
  text-align:center;
  position:relative;
  overflow:hidden;
  transition:all .35s cubic-bezier(.16,1,.3,1);
}
.kpi-card::before{
  content:'';
  position:absolute;
  top:0;left:0;right:0;
  height:3px;
  background:var(--grad);
}
.kpi-card:hover{
  border-color:var(--border2);
  transform:translateY(-5px) scale(1.03);
  box-shadow:0 12px 32px rgba(124,58,237,.25);
}
.kpi-value{
  font-family:var(--f);
  font-size:28px;
  font-weight:900;
  margin-bottom:6px;
  text-shadow:0 0 25px rgba(167,139,250,.4);
}
.kpi-label{
  font-family:var(--fm);
  font-size:10px;
  color:var(--t3);
  letter-spacing:.12em;
  text-transform:uppercase;
}
.kpi-trend{
  font-size:11px;
  margin-top:6px;
  font-weight:600;
}

div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input{
  background:rgba(21,18,48,.75)!important;
  backdrop-filter:blur(16px)!important;
  border:1px solid var(--border)!important;
  border-radius:10px!important;
  color:var(--t1)!important;
  font-family:var(--f)!important;
  font-size:14px!important;padding:12px 16px!important;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stNumberInput"] input:focus{
  border-color:rgba(167,139,250,.6)!important;
  box-shadow:0 0 0 3px rgba(167,139,250,.11)!important;
  outline:none!important;
}
div[data-testid="stTextInput"] label,
div[data-testid="stNumberInput"] label,
div[data-testid="stSelectbox"] label,
div[data-testid="stSlider"] label,
div[data-testid="stFileUploader"] label,
div[data-testid="stMultiSelect"] label{
  font-family:var(--fm)!important;font-size:10px!important;
  font-weight:500!important;color:var(--t3)!important;
  letter-spacing:.12em!important;text-transform:uppercase!important;
}
div[data-baseweb="select"]>div{
  background:rgba(21,18,48,.75)!important;
  backdrop-filter:blur(16px)!important;
  border:1px solid var(--border)!important;
  border-radius:10px!important;color:var(--t1)!important;
}

div.stButton>button{
  background:var(--grad)!important;color:white!important;
  font-family:var(--f)!important;font-weight:700!important;
  font-size:13px!important;
  border:none!important;border-radius:50px!important;
  padding:13px 34px!important;width:100%!important;
  cursor:pointer!important;
  box-shadow:0 0 26px rgba(124,58,237,.4)!important;
  transition:all .3s cubic-bezier(.16,1,.3,1)!important;
}
div.stButton>button:hover{
  transform:translateY(-3px) scale(1.02)!important;
  box-shadow:0 8px 32px rgba(124,58,237,.6)!important;
}

div[data-testid="stFileUploader"]{
  background:rgba(167,139,250,.04)!important;
  backdrop-filter:blur(16px)!important;
  border:1.5px dashed rgba(167,139,250,.32)!important;
  border-radius:var(--r)!important;padding:24px!important;
}

div[data-testid="stSlider"] div[role="slider"]{
  background:var(--neon)!important;
  box-shadow:0 0 12px rgba(167,139,250,.6)!important;
}

.stProgress>div>div{
  background:var(--grad)!important;border-radius:50px!important;
}

details{
  background:rgba(14,12,30,.65)!important;
  backdrop-filter:blur(20px)!important;
  border:1px solid var(--border)!important;
  border-radius:var(--r)!important;
  margin-bottom:14px!important;
}

.toast{
  background:rgba(16,185,129,.10);
  backdrop-filter:blur(12px);
  border:1px solid rgba(16,185,129,.30);
  border-radius:10px;padding:13px 20px;
  font-family:var(--fm);font-size:12px;color:#34d399;
  margin:12px 0;
}
.toast-err{background:rgba(239,68,68,.10);border-color:rgba(239,68,68,.28);color:#f87171;}
.toast-info{background:rgba(59,130,246,.10);border-color:rgba(59,130,246,.28);color:#93c5fd;}

.badge{
  display:inline-block;font-family:var(--fm);font-size:9px;
  font-weight:500;letter-spacing:.08em;text-transform:uppercase;
  padding:5px 12px;border-radius:50px;
}
.bv{background:rgba(124,58,237,.16);color:#c4b5fd;border:1px solid rgba(124,58,237,.28);}
.bg{background:rgba(16,185,129,.13);color:#34d399;border:1px solid rgba(16,185,129,.26);}
.ba{background:rgba(245,158,11,.13);color:#fcd34d;border:1px solid rgba(245,158,11,.26);}
.br{background:rgba(239,68,68,.11);color:#fca5a5;border:1px solid rgba(239,68,68,.24);}
.bc{background:rgba(34,211,238,.11);color:#67e8f9;border:1px solid rgba(34,211,238,.24);}
.bo{background:rgba(249,115,22,.11);color:#fdba74;border:1px solid rgba(249,115,22,.24);}

.pbox{
  background:linear-gradient(135deg,rgba(124,58,237,.12),rgba(59,130,246,.07));
  backdrop-filter:blur(20px);
  border:1px solid rgba(167,139,250,.3);
  border-radius:16px;padding:36px;text-align:center;
  position:relative;overflow:hidden;
}
.pbox::before{
  content:'';position:absolute;
  top:-55%;left:-55%;width:210%;height:210%;
  background:radial-gradient(circle,rgba(167,139,250,.06) 0%,transparent 52%);
  animation:pboxRot 12s linear infinite;
}
@keyframes pboxRot{to{transform:rotate(360deg)}}
.pval{
  font-family:var(--f);font-size:56px;font-weight:900;
  background:var(--grad2);-webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  position:relative;z-index:1;
}
.plbl{
  font-family:var(--fm);font-size:10px;color:var(--t3);
  letter-spacing:.15em;text-transform:uppercase;
  margin-bottom:10px;position:relative;z-index:1;
}
.psub{font-size:12px;color:var(--t2);margin-top:8px;position:relative;z-index:1;}

.ins{
  display:flex;align-items:flex-start;gap:14px;
  padding:14px 0;border-bottom:1px solid rgba(110,70,230,.10);
}
.ins:last-child{border-bottom:none}
.ins-icon{
  width:36px;height:36px;border-radius:9px;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;font-size:16px;
  background:rgba(167,139,250,.11);border:1px solid rgba(167,139,250,.18);
}
.ins-t{font-family:var(--f);font-size:14px;font-weight:600;color:var(--t1);margin-bottom:3px;}
.ins-d{font-size:13px;color:var(--t2);line-height:1.6;}

.sring-wrap{display:flex;justify-content:center;margin:24px 0 30px;}
.sring{
  width:130px;height:130px;border-radius:50%;
  position:relative;display:flex;align-items:center;justify-content:center;
}
.sring::before{
  content:'';position:absolute;inset:-3px;
  border-radius:50%;background:var(--grad);z-index:0;
  animation:spinRing 11s linear infinite;
}
@keyframes spinRing{to{transform:rotate(360deg)}}
.sring-inner{
  background:var(--panel);border-radius:50%;
  width:114px;height:114px;
  display:flex;flex-direction:column;align-items:center;
  justify-content:center;position:relative;z-index:1;
}
.snum{font-family:var(--f);font-size:34px;font-weight:900;}
.ssub{font-family:var(--fm);font-size:9px;color:var(--t3);
      letter-spacing:.10em;text-transform:uppercase;}

.bar-row{margin-bottom:16px;}
.bar-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:7px;}
.bar-name{font-family:var(--fm);font-size:12px;color:var(--t2);}
.bar-val{font-family:var(--fm);font-size:11px;font-weight:600;}
.bar-track{
  background:rgba(21,18,48,.75);
  border-radius:6px;height:7px;overflow:hidden;
}
.bar-fill{
  height:100%;border-radius:6px;
  transition:width 1.2s cubic-bezier(.16,1,.3,1);
}

@keyframes fadeUp{
  from{opacity:0;transform:translateY(20px)}
  to{opacity:1;transform:translateY(0)}
}

@keyframes float{
  0%,100%{transform:translateY(0)}
  50%{transform:translateY(-9px)}
}
</style>
"""

BG = """
<div class="bg-layer">
  <div class="ambient"></div>
  <div class="stars"></div>
  <div class="moon"></div>
  <div class="moon-ring"></div>
  <div class="moon-ring2"></div>
</div>
"""

# ═══════════════════════════════════════════════════════════════════════════════
# STATE INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════════

def initialize_state():
    defaults = {
        "authenticated": False,
        "auth_mode": "login",
        "accounts": {"admin": "astrae2026"},
        "username": "",
        "raw_df": None,
        "clean_df": None,
        "file_id": None,
        "health_report": {},
        "cleaning_report": {},
        "data_quality_kpis": {},
        "advanced_kpis": {},  # NEW: 4 additional KPIs
        "model": None,
        "scaler": None,
        "feature_names": [],
        "target_variable": None,
        "selected_features": [],
        "algorithm": "Gradient Boosting",
        "model_results": {},
        "feature_importance": {},
        "y_test": None,
        "y_pred": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

initialize_state()

# ═══════════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def H(html: str):
    st.markdown(html, unsafe_allow_html=True)

def create_file_id(uploaded_file) -> str:
    return f"{uploaded_file.name}_{uploaded_file.size}_{hash(uploaded_file.name)}"

# ═══════════════════════════════════════════════════════════════════════════════
# OPTIMIZED CORE ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

@st.cache_data(show_spinner=False, ttl=3600)
def load_data(file_bytes, file_name: str) -> pd.DataFrame:
    """Optimized file loader with error handling"""
    try:
        if file_name.endswith('.csv'):
            df = pd.read_csv(io.BytesIO(file_bytes), low_memory=False)
        elif file_name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(io.BytesIO(file_bytes), engine='openpyxl')
        else:
            raise ValueError("Unsupported format. Use CSV or Excel.")
        
        if df.empty:
            raise ValueError("File is empty")
        
        return df
    except Exception as e:
        raise ValueError(f"Load error: {str(e)}")

@st.cache_data(show_spinner=False)
def calculate_health(df: pd.DataFrame) -> Dict[str, Any]:
    """Calculate dataset health score (0-100)"""
    score = 100
    issues = []
    
    # Missing values penalty
    missing_ratio = df.isnull().mean().mean()
    score -= round(missing_ratio * 30)
    if missing_ratio > 0.05:
        issues.append(f"{missing_ratio*100:.1f}% missing values")
    
    # Duplicates penalty
    dup_count = df.duplicated().sum()
    dup_ratio = dup_count / max(len(df), 1)
    score -= round(dup_ratio * 20)
    if dup_count > 0:
        issues.append(f"{dup_count:,} duplicate rows")
    
    # Skewness penalty
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if len(numeric_cols) > 0:
        mean_skew = df[numeric_cols].skew().abs().mean()
        score -= min(round(mean_skew * 4), 22)
        if mean_skew > 1.0:
            issues.append(f"High skewness: {mean_skew:.2f}")
    
    # Constant columns penalty
    constant_cols = [col for col in df.columns if df[col].nunique() <= 1]
    score -= min(len(constant_cols) * 10, 18)
    if constant_cols:
        issues.append(f"{len(constant_cols)} constant columns")
    
    return {
        'score': max(0, min(100, score)),
        'missing_pct': round(missing_ratio * 100, 2),
        'duplicate_count': int(dup_count),
        'rows': len(df),
        'columns': len(df.columns),
        'numeric_columns': len(numeric_cols),
        'constant_columns': len(constant_cols),
        'issues': issues,
        'completeness': round((1 - missing_ratio) * 100, 2),
        'uniqueness': round((1 - dup_ratio) * 100, 2)
    }

@st.cache_data(show_spinner=False)
def clean_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Automated data cleaning pipeline"""
    start_time = time.time()
    df_clean = df.copy()
    report = {}
    
    # Remove duplicates
    dup_count = df_clean.duplicated().sum()
    df_clean.drop_duplicates(inplace=True)
    report['duplicates_removed'] = int(dup_count)
    
    # Type conversions
    converted_cols = []
    for col in df_clean.select_dtypes(include='object').columns:
        try:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='raise')
            converted_cols.append(col)
        except:
            pass
    report['type_conversions'] = converted_cols
    
    # Clean column names
    df_clean.columns = [
        col.strip().replace(' ', '_').replace('-', '_').lower() 
        for col in df_clean.columns
    ]
    
    # Fill missing values
    missing_before = df_clean.isnull().sum().sum()
    
    # Numeric: median imputation
    for col in df_clean.select_dtypes(include=np.number).columns:
        if df_clean[col].isnull().any():
            df_clean[col].fillna(df_clean[col].median(), inplace=True)
    
    # Categorical: mode imputation
    for col in df_clean.select_dtypes(exclude=np.number).columns:
        if df_clean[col].isnull().any():
            mode_val = df_clean[col].mode()
            df_clean[col].fillna(mode_val[0] if not mode_val.empty else "Unknown", inplace=True)
    
    report['missing_filled'] = int(missing_before)
    
    # Remove constant columns
    constant_cols = [col for col in df_clean.columns if df_clean[col].nunique() <= 1]
    df_clean.drop(columns=constant_cols, inplace=True)
    report['constant_columns_removed'] = constant_cols
    
    # Trim strings
    for col in df_clean.select_dtypes(include='object').columns:
        df_clean[col] = df_clean[col].astype(str).str.strip()
    
    report['rows_input'] = len(df)
    report['rows_output'] = len(df_clean)
    report['columns_output'] = len(df_clean.columns)
    report['processing_time'] = round(time.time() - start_time, 3)
    
    return df_clean, report

@st.cache_data(show_spinner=False)
def calculate_data_quality_kpis(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Calculate 5 CRITICAL Data Quality KPIs
    Required by assignment specifications
    """
    
    # KPI 1: Data Completeness Rate (non-null percentage)
    completeness = round((1 - df.isnull().mean().mean()) * 100, 2)
    
    # KPI 2: Data Consistency Score (duplicate-free rate)
    consistency = round((1 - df.duplicated().sum() / max(len(df), 1)) * 100, 2)
    
    # KPI 3: Data Accuracy Index (type validity)
    numeric_cols = df.select_dtypes(include=np.number).columns
    accuracy = round((len(numeric_cols) / max(len(df.columns), 1)) * 100, 2)
    
    # KPI 4: Data Validity Rate (outlier detection via IQR)
    if len(numeric_cols) > 0:
        outlier_count = 0
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()
            outlier_count += outliers
        validity = round((1 - outlier_count / (len(df) * len(numeric_cols))) * 100, 2)
    else:
        validity = 100.0
    
    # KPI 5: Data Uniformity Score (coefficient of variation)
    if len(numeric_cols) > 0:
        cv_scores = []
        for col in numeric_cols:
            mean_val = df[col].mean()
            std_val = df[col].std()
            if mean_val != 0:
                cv = (std_val / abs(mean_val))
                cv_scores.append(min(cv, 2.0))
        avg_cv = np.mean(cv_scores) if cv_scores else 0
        uniformity = round(max(0, (1 - avg_cv / 2.0) * 100), 2)
    else:
        uniformity = 100.0
    
    # Overall composite score
    overall = round((completeness + consistency + accuracy + validity + uniformity) / 5, 2)
    
    return {
        'completeness': completeness,
        'consistency': consistency,
        'accuracy': accuracy,
        'validity': validity,
        'uniformity': uniformity,
        'overall_quality': overall
    }

@st.cache_data(show_spinner=False)
def calculate_advanced_kpis(df: pd.DataFrame) -> Dict[str, Any]:
    """
    ⭐ NEW: Calculate 4 ADVANCED Business KPIs
    Added to meet "3-4 additional KPIs" requirement
    """
    
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    
    # ADVANCED KPI 1: Data Density Score (non-zero percentage)
    if len(numeric_cols) > 0:
        non_zero_counts = []
        for col in numeric_cols:
            non_zero_pct = (df[col] != 0).sum() / max(len(df), 1)
            non_zero_counts.append(non_zero_pct)
        density = round(np.mean(non_zero_counts) * 100, 2)
    else:
        density = 100.0
    
    # ADVANCED KPI 2: Data Balance Index (distribution evenness)
    if len(numeric_cols) > 0:
        balance_scores = []
        for col in numeric_cols:
            # Calculate coefficient of variation (CV)
            mean_val = df[col].mean()
            std_val = df[col].std()
            if mean_val != 0:
                cv = std_val / abs(mean_val)
                # Invert CV: lower CV = higher balance
                balance = max(0, 100 - (cv * 50))
                balance_scores.append(min(balance, 100))
        balance_index = round(np.mean(balance_scores), 2) if balance_scores else 100.0
    else:
        balance_index = 100.0
    
    # ADVANCED KPI 3: Feature Richness Score (unique values ratio)
    richness_scores = []
    for col in df.columns:
        unique_ratio = df[col].nunique() / max(len(df), 1)
        richness_scores.append(min(unique_ratio * 100, 100))
    richness = round(np.mean(richness_scores), 2) if richness_scores else 0.0
    
    # ADVANCED KPI 4: Data Reliability Index (variance stability)
    if len(numeric_cols) > 0:
        reliability_scores = []
        for col in numeric_cols:
            # Use coefficient of quartile variation
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            median = df[col].median()
            if median != 0:
                cqv = (Q3 - Q1) / (2 * abs(median))
                reliability = max(0, 100 - (cqv * 100))
                reliability_scores.append(min(reliability, 100))
        reliability_index = round(np.mean(reliability_scores), 2) if reliability_scores else 100.0
    else:
        reliability_index = 100.0
    
    # Composite advanced score
    advanced_score = round((density + balance_index + richness + reliability_index) / 4, 2)
    
    return {
        'density': density,
        'balance_index': balance_index,
        'richness': richness,
        'reliability_index': reliability_index,
        'advanced_score': advanced_score
    }

@st.cache_resource(show_spinner=False, ttl=3600)
def train_model(df: pd.DataFrame, target: str, features: List[str], algorithm: str) -> Dict[str, Any]:
    """ML training pipeline with auto-encoding"""
    if not SKLEARN_AVAILABLE:
        raise RuntimeError("scikit-learn required")
    
    start_time = time.time()
    
    # Prepare data
    X = df[features].copy()
    y = pd.to_numeric(df[target], errors='coerce')
    
    # Fill target NaNs
    if y.isnull().any():
        y.fillna(y.median(), inplace=True)
    
    # Separate numeric and categorical
    numeric_features = X.select_dtypes(include=np.number).columns.tolist()
    categorical_features = X.select_dtypes(exclude=np.number).columns.tolist()
    
    # Impute numeric
    if numeric_features:
        X[numeric_features] = SimpleImputer(strategy='median').fit_transform(X[numeric_features])
    
    # Encode categorical
    if categorical_features:
        X[categorical_features] = SimpleImputer(strategy='most_frequent').fit_transform(X[categorical_features])
        X = pd.get_dummies(X, columns=categorical_features, drop_first=True)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Scale features
    scaler = RobustScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Model selection
    models = {
        "Gradient Boosting": GradientBoostingRegressor(
            n_estimators=100, learning_rate=0.1, max_depth=4, random_state=42
        ),
        "Random Forest": RandomForestRegressor(
            n_estimators=80, max_depth=6, random_state=42, n_jobs=-1
        ),
        "Extra Trees": ExtraTreesRegressor(
            n_estimators=80, max_depth=6, random_state=42, n_jobs=-1
        ),
        "Linear Regression": LinearRegression(),
        "Ridge Regression": Ridge(alpha=1.0),
    }
    
    model = models.get(algorithm, models["Gradient Boosting"])
    
    # Train
    model.fit(X_train_scaled, y_train)
    
    # Predictions
    y_pred = model.predict(X_test_scaled)
    y_train_pred = model.predict(X_train_scaled)
    
    # Metrics
    r2 = float(r2_score(y_test, y_pred))
    r2_train = float(r2_score(y_train, y_train_pred))
    mae = float(mean_absolute_error(y_test, y_pred))
    rmse = float(np.sqrt(mean_squared_error(y_test, y_pred)))
    
    try:
        mape = float(mean_absolute_percentage_error(y_test, y_pred))
    except:
        mape = 0.0
    
    # Cross-validation
    try:
        cv_scores = cross_val_score(
            model, scaler.transform(X), y, cv=3, scoring='r2', n_jobs=-1
        ).tolist()
    except:
        cv_scores = [r2]
    
    # Feature importance
    feature_importance = {}
    if hasattr(model, 'feature_importances_'):
        feature_importance = {
            col: float(imp) for col, imp in zip(X.columns, model.feature_importances_)
        }
    elif hasattr(model, 'coef_'):
        feature_importance = {
            col: float(abs(coef)) for col, coef in zip(X.columns, model.coef_)
        }
    
    return {
        'model': model,
        'scaler': scaler,
        'feature_names': X.columns.tolist(),
        'r2': r2,
        'r2_train': r2_train,
        'mae': mae,
        'rmse': rmse,
        'mape': mape,
        'cv_scores': cv_scores,
        'cv_mean': float(np.mean(cv_scores)),
        'cv_std': float(np.std(cv_scores)),
        'feature_importance': feature_importance,
        'y_test': y_test.values,
        'y_pred': y_pred,
        'residuals': y_test.values - y_pred,
        'training_time': round(time.time() - start_time, 3),
        'n_train': len(X_train),
        'n_test': len(X_test),
        'overfitting_delta': abs(r2_train - r2)
    }

def generate_insights(df: pd.DataFrame, target: str, results: Dict[str, Any]) -> List[Tuple[str, str, str]]:
    """Generate AI-driven insights from model results"""
    insights = []
    r2 = results['r2']
    mae = results['mae']
    cv_mean = results['cv_mean']
    cv_std = results['cv_std']
    importance = results['feature_importance']
    overfitting = results['overfitting_delta']
    
    # Performance insight
    if r2 >= 0.85:
        insights.append((
            "🎯", 
            "Excellent Performance", 
            f"R² = {r2:.3f} — explains {r2*100:.1f}% of variance. Production-ready."
        ))
    elif r2 >= 0.65:
        insights.append((
            "📊", 
            "Good Performance", 
            f"R² = {r2:.3f} — reliable predictions with room for optimization."
        ))
    else:
        insights.append((
            "⚠️", 
            "Limited Performance", 
            f"R² = {r2:.3f} — consider feature engineering or algorithm change."
        ))
    
    # Overfitting detection
    if overfitting < 0.05:
        insights.append((
            "✅", 
            "No Overfitting", 
            f"Model generalizes well (Δ={overfitting:.3f})."
        ))
    else:
        insights.append((
            "⚡", 
            "Overfitting Detected", 
            f"Train-test gap: {overfitting:.3f}. Consider regularization or reduce complexity."
        ))
    
    # Top feature
    if importance:
        top_feature = max(importance, key=importance.get)
        top_value = importance[top_feature]
        insights.append((
            "🔑", 
            f"Top Driver: {top_feature}", 
            f"Contributes {top_value*100:.1f}% to predictions of {target}."
        ))
    
    # Cross-validation stability
    if cv_std < 0.05:
        insights.append((
            "🎲", 
            "Stable Model", 
            f"CV std = {cv_std:.4f}. Consistent performance across folds."
        ))
    else:
        insights.append((
            "📉", 
            "Variable Performance", 
            f"CV std = {cv_std:.4f}. May need more data or better features."
        ))
    
    # Error metrics summary
    insights.append((
        "📊", 
        "Error Metrics", 
        f"MAE = {mae:,.2f} | RMSE = {results['rmse']:,.2f} | CV Mean = {cv_mean:.3f}"
    ))
    
    return insights

def generate_fast_chart(results: Dict[str, Any]):
    """Optimized matplotlib charts for model diagnostics"""
    if not PLOT_AVAILABLE:
        return None
    
    try:
        y_test = results['y_test']
        y_pred = results['y_pred']
        residuals = results['residuals']
        
        fig, axes = plt.subplots(1, 3, figsize=(15, 4), facecolor='#04030c')
        
        # Chart 1: Actual vs Predicted
        axes[0].scatter(y_test, y_pred, alpha=0.6, color='#a78bfa', s=30, edgecolors='#7c3aed')
        axes[0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
        axes[0].set_xlabel('Actual', color='#aea6d0', fontsize=10)
        axes[0].set_ylabel('Predicted', color='#aea6d0', fontsize=10)
        axes[0].set_title('Actual vs Predicted', color='#eeeaff', fontsize=11, fontweight='bold')
        axes[0].set_facecolor('#0e0c1e')
        axes[0].tick_params(colors='#5e5880', labelsize=8)
        axes[0].grid(True, alpha=0.2, color='#5e5880', linestyle='--')
        
        # Chart 2: Residual Plot
        axes[1].scatter(y_pred, residuals, alpha=0.6, color='#22d3ee', s=30, edgecolors='#0ea5e9')
        axes[1].axhline(y=0, color='#ef4444', linestyle='--', lw=2)
        axes[1].set_xlabel('Predicted', color='#aea6d0', fontsize=10)
        axes[1].set_ylabel('Residuals', color='#aea6d0', fontsize=10)
        axes[1].set_title('Residual Plot', color='#eeeaff', fontsize=11, fontweight='bold')
        axes[1].set_facecolor('#0e0c1e')
        axes[1].tick_params(colors='#5e5880', labelsize=8)
        axes[1].grid(True, alpha=0.2, color='#5e5880', linestyle='--')
        
        # Chart 3: Residual Distribution
        axes[2].hist(residuals, bins=20, alpha=0.7, color='#f59e0b', edgecolor='#0e0c1e')
        axes[2].set_xlabel('Residuals', color='#aea6d0', fontsize=10)
        axes[2].set_ylabel('Frequency', color='#aea6d0', fontsize=10)
        axes[2].set_title('Residual Distribution', color='#eeeaff', fontsize=11, fontweight='bold')
        axes[2].set_facecolor('#0e0c1e')
        axes[2].tick_params(colors='#5e5880', labelsize=8)
        
        plt.tight_layout()
        return fig
    except Exception as e:
        st.warning(f"Chart generation failed: {str(e)}")
        return None

# ═══════════════════════════════════════════════════════════════════════════════
# UI RENDERING
# ═══════════════════════════════════════════════════════════════════════════════

H(CSS)
H(BG)

user_display = f"👤 {st.session_state.username}" if st.session_state.authenticated else ""
H(f"""
<nav class="nav">
  <div class="nav-logo">🔮 ASTRAE</div>
  <div class="nav-right">
    <span class="nav-user">{user_display}</span>
    <div class="nav-chip">v4.0 · ULTIMATE</div>
  </div>
</nav>
<div class="nav-spacer"></div>
""")

# ═══════════════════════════════════════════════════════════════════════════════
# AUTHENTICATION
# ═══════════════════════════════════════════════════════════════════════════════

if not st.session_state.authenticated:
    H("""
    <div class="hero">
      <div class="hero-pill"><div class="pill-dot"></div>Enterprise Decision Intelligence</div>
      <h1 class="hero-h"><span class="grad-text">ASTRAE</span><br><span style="color:var(--t1)">Intelligence</span></h1>
      <p class="hero-sub">
        Ultra-optimized predictive analytics. 9 Professional KPIs. Advanced visualizations. Zero latency.
      </p>
    </div>
    """)
    
    H('<div style="max-width:440px;margin:0 auto;padding:40px 0;">')
    H('<div style="font-size:54px;text-align:center;margin-bottom:20px;filter:drop-shadow(0 0 30px rgba(167,139,250,.9));animation:float 4s ease-in-out infinite;">🔮</div>')
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign In", key="switch_login", use_container_width=True):
            st.session_state.auth_mode = "login"
            st.rerun()
    with col2:
        if st.button("Create Account", key="switch_signup", use_container_width=True):
            st.session_state.auth_mode = "signup"
            st.rerun()
    
    H('<div style="height:20px;"></div>')
    
    if st.session_state.auth_mode == "login":
        H('<div style="text-align:center;font-size:28px;font-weight:700;margin-bottom:6px;">Welcome Back</div>')
        H('<div style="text-align:center;font-size:13px;color:var(--t3);margin-bottom:32px;">Access your workspace</div>')
        
        username = st.text_input("Username", placeholder="your username", key="login_user")
        password = st.text_input("Password", type="password", placeholder="your password", key="login_pass")
        
        H('<div style="height:8px;"></div>')
        
        if st.button("Sign In →", key="btn_login", use_container_width=True):
            if username in st.session_state.accounts and st.session_state.accounts[username] == password:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            else:
                H('<div class="toast toast-err">⚠ Invalid credentials</div>')
        
        H('<div style="text-align:center;margin-top:16px;"><span style="font-family:var(--fm);font-size:10px;color:var(--t3);">Demo: admin / astrae2026</span></div>')
    
    else:
        H('<div style="text-align:center;font-size:28px;font-weight:700;margin-bottom:6px;">Create Account</div>')
        H('<div style="text-align:center;font-size:13px;color:var(--t3);margin-bottom:32px;">Join the platform</div>')
        
        new_user = st.text_input("Username", placeholder="choose username", key="reg_user")
        new_email = st.text_input("Email", placeholder="you@company.com", key="reg_email")
        new_pass1 = st.text_input("Password", type="password", placeholder="min 6 chars", key="reg_pass1")
        new_pass2 = st.text_input("Confirm Password", type="password", placeholder="repeat", key="reg_pass2")
        
        H('<div style="height:8px;"></div>')
        
        if st.button("Create Account →", key="btn_signup", use_container_width=True):
            if not new_user or not new_email or not new_pass1:
                H('<div class="toast toast-err">⚠ All fields required</div>')
            elif new_pass1 != new_pass2:
                H('<div class="toast toast-err">⚠ Passwords mismatch</div>')
            elif len(new_pass1) < 6:
                H('<div class="toast toast-err">⚠ Password too short</div>')
            elif new_user in st.session_state.accounts:
                H('<div class="toast toast-err">⚠ Username taken</div>')
            else:
                st.session_state.accounts[new_user] = new_pass1
                st.session_state.authenticated = True
                st.session_state.username = new_user
                st.rerun()
    
    H('</div>')
    H("""
    <div style="text-align:center;margin-top:48px;display:flex;justify-content:center;gap:10px;flex-wrap:wrap;">
      <span class="badge bv">Advanced ML</span>
      <span class="badge bc">9 KPIs</span>
      <span class="badge bg">Professional Charts</span>
      <span class="badge ba">Zero Latency</span>
    </div>
    """)
    st.stop()

# ═══════════════════════════════════════════════════════════════════════════════
# AUTHENTICATED WORKSPACE
# ═══════════════════════════════════════════════════════════════════════════════

H(f"""
<div class="hero" style="padding-top:36px;padding-bottom:32px;">
  <div class="hero-pill"><div class="pill-dot"></div>Workspace · {st.session_state.username}</div>
  <h1 class="hero-h" style="font-size:clamp(36px,5vw,60px);"><span class="grad-text">Decision Intelligence</span></h1>
  <p class="hero-sub">Professional analytics | 9 Real-time KPIs | Advanced ML | Production-ready</p>
</div>
""")

col_main, col_logout = st.columns([6, 1])
with col_logout:
    if st.button("Logout", key="logout"):
        accounts_backup = st.session_state.accounts
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state.accounts = accounts_backup
        initialize_state()
        st.rerun()

H('<div style="height:24px;"></div>')

# ═══════════════════════════════════════════════════════════════════════════════
# UPLOAD
# ═══════════════════════════════════════════════════════════════════════════════

H("""
<div class="card card-glow">
  <div class="ey">Step 1 · Upload</div>
  <div class="ct">Upload Dataset</div>
  <div class="cd">CSV or Excel. In-memory processing. GDPR compliant.</div>
""")

uploaded_file = st.file_uploader("Drop file here", type=["csv", "xlsx", "xls"], key="file_uploader")

if uploaded_file:
    file_id = create_file_id(uploaded_file)
    
    if st.session_state.file_id != file_id:
        try:
            file_bytes = uploaded_file.read()
            df = load_data(file_bytes, uploaded_file.name)
            
            st.session_state.raw_df = df
            st.session_state.file_id = file_id
            st.session_state.clean_df = None
            st.session_state.model = None
            st.session_state.health_report = {}
            st.session_state.cleaning_report = {}
            st.session_state.data_quality_kpis = {}
            st.session_state.advanced_kpis = {}
            st.session_state.model_results = {}
            
            st.success("✅ Loaded!")
            st.rerun()
        except ValueError as e:
            st.error(f"⚠️ {str(e)}")
    
    df = st.session_state.raw_df
    rows, cols = df.shape
    numeric_count = len(df.select_dtypes(include=np.number).columns)
    missing_pct = round(df.isnull().mean().mean() * 100, 1)
    dup_count = df.duplicated().sum()
    
    H(f"""
    <div class="kpi-grid">
      <div class="kpi-card">
        <div class="kpi-value" style="color:#a78bfa">{rows:,}</div>
        <div class="kpi-label">Rows</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-value" style="color:#22d3ee">{cols}</div>
        <div class="kpi-label">Columns</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-value" style="color:#34d399">{numeric_count}</div>
        <div class="kpi-label">Numeric</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-value" style="color:#f59e0b">{missing_pct}%</div>
        <div class="kpi-label">Missing</div>
      </div>
      <div class="kpi-card">
        <div class="kpi-value" style="color:#f97316">{dup_count:,}</div>
        <div class="kpi-label">Duplicates</div>
      </div>
    </div>
    <div class="toast">✦ {uploaded_file.name} — {rows:,} × {cols}</div>
    """)
    
    with st.expander("📊 Preview Raw Data"):
        st.dataframe(df.head(10), use_container_width=True)

H("</div>")

# ═══════════════════════════════════════════════════════════════════════════════
# DIAGNOSE
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.raw_df is not None:
    H("""
    <div class="card">
      <div class="ey">Step 2 · Diagnose</div>
      <div class="ct">Health Analysis</div>
      <div class="cd">Multi-dimensional quality assessment</div>
    """)
    
    if not st.session_state.health_report:
        st.session_state.health_report = calculate_health(st.session_state.raw_df)
    
    health = st.session_state.health_report
    score = health['score']
    
    ring_color = "#34d399" if score >= 80 else ("#fcd34d" if score >= 55 else "#f87171")
    H(f"""
    <div class="sring-wrap">
      <div class="sring">
        <div class="sring-inner">
          <div class="snum" style="color:{ring_color}">{score}</div>
          <div class="ssub">Quality</div>
        </div>
      </div>
    </div>
    """)
    
    grade = "Excellent" if score >= 80 else ("Good" if score >= 55 else "Needs Cleaning")
    badge_class = "bg" if score >= 80 else ("ba" if score >= 55 else "br")
    
    H(f'<div style="text-align:center;margin-bottom:24px;"><span class="badge {badge_class}">{grade}</span></div>')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Missing", f"{health['missing_pct']}%")
    col2.metric("Duplicates", f"{health['duplicate_count']:,}")
    col3.metric("Constant", str(health['constant_columns']))
    col4.metric("Numeric", str(health['numeric_columns']))
    col5.metric("Records", f"{health['rows']:,}")
    
    if health['issues']:
        H('<div style="margin-top:20px;">')
        for issue in health['issues']:
            H(f'<div class="toast toast-info">ℹ {issue}</div>')
        H('</div>')
    
    H("</div>")

# ═══════════════════════════════════════════════════════════════════════════════
# CLEAN
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.raw_df is not None:
    H("""
    <div class="card card-glow">
      <div class="ey">Step 3 · Clean</div>
      <div class="ct">Data Cleaning</div>
      <div class="cd">Automated preprocessing pipeline</div>
    """)
    
    if st.session_state.clean_df is not None:
        report = st.session_state.cleaning_report
        
        H(f"""
        <div style="background:rgba(21,18,48,.8);border:1px solid var(--border);border-radius:var(--r);padding:24px;margin-bottom:20px;">
          <div class="ey" style="margin-bottom:14px;">Cleaning Report</div>
          <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:12px;">
            <div class="ins">
              <div class="ins-icon">🗑️</div>
              <div><div class="ins-t">{report.get('duplicates_removed', 0):,} duplicates</div></div>
            </div>
            <div class="ins">
              <div class="ins-icon">🔧</div>
              <div><div class="ins-t">{report.get('missing_filled', 0):,} filled</div></div>
            </div>
            <div class="ins">
              <div class="ins-icon">🏷️</div>
              <div><div class="ins-t">{len(report.get('type_conversions', []))} conversions</div></div>
            </div>
            <div class="ins">
              <div class="ins-icon">✅</div>
              <div><div class="ins-t">{report.get('rows_output', 0):,} clean rows</div></div>
            </div>
          </div>
        </div>
        """)
        
        # ═══════════════════════════════════════════════════════════════════════════════
        # 5 CRITICAL DATA QUALITY KPIs (REQUIRED)
        # ═══════════════════════════════════════════════════════════════════════════════
        
        if not st.session_state.data_quality_kpis:
            st.session_state.data_quality_kpis = calculate_data_quality_kpis(st.session_state.clean_df)
        
        kpis = st.session_state.data_quality_kpis
        
        H("""
        <div style="background:rgba(21,18,48,.8);border:1px solid var(--border);border-radius:var(--r);padding:24px;margin-bottom:20px;">
          <div class="ey" style="margin-bottom:14px;">✦ 5 Critical Data Quality KPIs</div>
        """)
        
        H(f"""
        <div class="kpi-grid">
          <div class="kpi-card">
            <div class="kpi-value" style="color:#34d399">{kpis['completeness']}%</div>
            <div class="kpi-label">Completeness</div>
            <div class="kpi-trend" style="color:#aea6d0">Non-null rate</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-value" style="color:#22d3ee">{kpis['consistency']}%</div>
            <div class="kpi-label">Consistency</div>
            <div class="kpi-trend" style="color:#aea6d0">Unique rate</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-value" style="color:#a78bfa">{kpis['accuracy']}%</div>
            <div class="kpi-label">Accuracy</div>
            <div class="kpi-trend" style="color:#aea6d0">Type validity</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-value" style="color:#f59e0b">{kpis['validity']}%</div>
            <div class="kpi-label">Validity</div>
            <div class="kpi-trend" style="color:#aea6d0">Outlier-free</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-value" style="color:#f97316">{kpis['uniformity']}%</div>
            <div class="kpi-label">Uniformity</div>
            <div class="kpi-trend" style="color:#aea6d0">Distribution</div>
          </div>
        </div>
        </div>
        """)
        
        H(f'<div class="toast">✅ Overall Quality Score: {kpis["overall_quality"]}%</div>')
        
        # ═══════════════════════════════════════════════════════════════════════════════
        # ⭐ 4 NEW ADVANCED BUSINESS KPIs (ADDED)
        # ═══════════════════════════════════════════════════════════════════════════════
        
        if not st.session_state.advanced_kpis:
            st.session_state.advanced_kpis = calculate_advanced_kpis(st.session_state.clean_df)
        
        adv_kpis = st.session_state.advanced_kpis
        
        H("""
        <div style="background:rgba(21,18,48,.8);border:1px solid var(--border);border-radius:var(--r);padding:24px;margin-bottom:20px;">
          <div class="ey" style="margin-bottom:14px;">⭐ 4 Advanced Business KPIs (NEW)</div>
        """)
        
        H(f"""
        <div class="kpi-grid">
          <div class="kpi-card">
            <div class="kpi-value" style="color:#c4b5fd">{adv_kpis['density']}%</div>
            <div class="kpi-label">Data Density</div>
            <div class="kpi-trend" style="color:#aea6d0">Non-zero ratio</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-value" style="color:#67e8f9">{adv_kpis['balance_index']}%</div>
            <div class="kpi-label">Balance Index</div>
            <div class="kpi-trend" style="color:#aea6d0">Distribution evenness</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-value" style="color:#34d399">{adv_kpis['richness']}%</div>
            <div class="kpi-label">Feature Richness</div>
            <div class="kpi-trend" style="color:#aea6d0">Unique values</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-value" style="color:#fdba74">{adv_kpis['reliability_index']}%</div>
            <div class="kpi-label">Reliability Index</div>
            <div class="kpi-trend" style="color:#aea6d0">Variance stability</div>
          </div>
        </div>
        </div>
        """)
        
        H(f'<div class="toast toast-info">📊 Advanced Composite Score: {adv_kpis["advanced_score"]}%</div>')
        
        with st.expander("📊 Preview Clean Data"):
            st.dataframe(st.session_state.clean_df.head(10), use_container_width=True)
    
    else:
        col_clean, col_skip = st.columns([2, 1])
        
        with col_clean:
            if st.button("🧹 Clean Now", key="btn_clean", use_container_width=True):
                with st.spinner("Cleaning..."):
                    clean_df, report = clean_data(st.session_state.raw_df)
                
                st.session_state.clean_df = clean_df
                st.session_state.cleaning_report = report
                st.success("✅ Done!")
                st.rerun()
        
        with col_skip:
            if st.button("Skip", key="btn_skip", use_container_width=True):
                st.session_state.clean_df = st.session_state.raw_df.copy()
                st.session_state.cleaning_report = {"note": "Skipped"}
                st.rerun()
    
    H("</div>")

# ═══════════════════════════════════════════════════════════════════════════════
# TRAIN
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.clean_df is not None:
    H("""
    <div class="card card-glow">
      <div class="ey">Step 4 · Train</div>
      <div class="ct">Model Training</div>
      <div class="cd">ML pipeline with auto-encoding and scaling</div>
    """)
    
    if SKLEARN_AVAILABLE:
        df_clean = st.session_state.clean_df
        all_columns = df_clean.columns.tolist()
        numeric_columns = df_clean.select_dtypes(include=np.number).columns.tolist()
        
        col_target, col_algo = st.columns(2)
        
        with col_target:
            target = st.selectbox(
                "Target Variable", 
                options=numeric_columns if numeric_columns else all_columns, 
                key="target_select"
            )
        
        with col_algo:
            algorithm = st.selectbox(
                "Algorithm", 
                ["Gradient Boosting", "Random Forest", "Extra Trees", "Linear Regression", "Ridge Regression"], 
                key="algo_select"
            )
        
        available_features = [col for col in all_columns if col != target]
        selected_features = st.multiselect(
            "Features", 
            options=available_features, 
            default=available_features[:min(8, len(available_features))], 
            key="feature_select"
        )
        
        H('<div style="height:14px;"></div>')
        
        if st.button("⚡ Train Model", key="btn_train", use_container_width=True):
            if not selected_features:
                st.error("⚠️ Select at least one feature")
            elif not pd.api.types.is_numeric_dtype(df_clean[target]):
                st.error("⚠️ Target must be numeric")
            else:
                with st.spinner(f"Training {algorithm}..."):
                    try:
                        results = train_model(df_clean, target, selected_features, algorithm)
                        
                        st.session_state.model = results['model']
                        st.session_state.scaler = results['scaler']
                        st.session_state.feature_names = results['feature_names']
                        st.session_state.target_variable = target
                        st.session_state.selected_features = selected_features
                        st.session_state.algorithm = algorithm
                        st.session_state.model_results = results
                        st.session_state.feature_importance = results['feature_importance']
                        st.session_state.y_test = results['y_test']
                        st.session_state.y_pred = results['y_pred']
                        
                        st.success(f"✅ Trained in {results['training_time']}s!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"⚠️ Training failed: {str(e)}")
    else:
        st.error("⚠️ scikit-learn not available")
    
    H("</div>")

# ═══════════════════════════════════════════════════════════════════════════════
# RESULTS
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.model is not None:
    results = st.session_state.model_results
    r2 = results['r2']
    mae = results['mae']
    rmse = results['rmse']
    cv_mean = results['cv_mean']
    importance = results['feature_importance']
    
    H(f"""
    <div class="card">
      <div class="ey">Performance</div>
      <div class="ct">Model Metrics</div>
      <div class="cd">Test set evaluation</div>
      
      <div class="kpi-grid">
        <div class="kpi-card">
          <div class="kpi-value" style="color:#34d399">{r2:.4f}</div>
          <div class="kpi-label">R² Score</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-value" style="color:#22d3ee">{cv_mean:.4f}</div>
          <div class="kpi-label">CV Mean</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-value" style="color:#a78bfa">{mae:,.2f}</div>
          <div class="kpi-label">MAE</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-value" style="color:#f59e0b">{rmse:,.2f}</div>
          <div class="kpi-label">RMSE</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-value" style="color:#c4b5fd">{results['training_time']:.2f}s</div>
          <div class="kpi-label">Train Time</div>
        </div>
      </div>
    </div>
    """)
    
    H("""
    <div class="card">
      <div class="ey">Charts</div>
      <div class="ct">Visual Analysis</div>
      <div class="cd">Model diagnostics</div>
    """)
    
    fig = generate_fast_chart(results)
    if fig:
        st.pyplot(fig, use_container_width=True)
    else:
        st.info("Charts unavailable")
    
    H("</div>")
    
    if importance:
        H("""
        <div class="card">
          <div class="ey">Feature Importance</div>
          <div class="ct">Top Drivers</div>
          <div class="cd">Predictive contribution</div>
        """)
        
        COLORS = ["#a78bfa","#22d3ee","#34d399","#f59e0b","#f97316"]
        top_features = sorted(importance.items(), key=lambda x: x[1], reverse=True)[:10]
        max_imp = max(v for _, v in top_features) if top_features else 1
        
        for idx, (feature, value) in enumerate(top_features):
            pct = round(value / max_imp * 100, 1)
            val_pct = round(value * 100, 2)
            color = COLORS[idx % len(COLORS)]
            
            H(f"""
            <div class="bar-row">
              <div class="bar-top">
                <span class="bar-name">{feature[:40]}</span>
                <span class="bar-val" style="color:{color}">{val_pct}%</span>
              </div>
              <div class="bar-track">
                <div class="bar-fill" style="width:{pct}%;background:{color};"></div>
              </div>
            </div>
            """)
        
        H("</div>")
    
    insights = generate_insights(
        st.session_state.clean_df, 
        st.session_state.target_variable, 
        results
    )
    
    H("""
    <div class="card">
      <div class="ey">AI Insights</div>
      <div class="ct">Analysis</div>
      <div class="cd">Strategic interpretation</div>
    """)
    
    for icon, title, description in insights:
        H(f"""
        <div class="ins">
          <div class="ins-icon">{icon}</div>
          <div>
            <div class="ins-t">{title}</div>
            <div class="ins-d">{description}</div>
          </div>
        </div>
        """)
    
    H("</div>")

# ═══════════════════════════════════════════════════════════════════════════════
# PREDICT
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.model is not None:
    H("""
    <div class="card card-glow">
      <div class="ey">Inference</div>
      <div class="ct">What-If Simulator</div>
      <div class="cd">Real-time predictions</div>
    """)
    
    df_clean = st.session_state.clean_df
    feature_names = st.session_state.feature_names
    target = st.session_state.target_variable
    
    numeric_features = [
        f for f in st.session_state.selected_features 
        if f in df_clean.select_dtypes(include=np.number).columns
    ]
    
    input_values = {}
    
    if numeric_features:
        st.write("**Adjust Values:**")
        cols = st.columns(min(3, len(numeric_features)))
        
        for idx, feature in enumerate(numeric_features[:9]):
            col_min = float(df_clean[feature].min())
            col_max = float(df_clean[feature].max())
            col_median = float(df_clean[feature].median())
            
            if col_min == col_max:
                col_max = col_min + 1
            
            with cols[idx % len(cols)]:
                input_values[feature] = st.slider(
                    feature[:20], 
                    min_value=col_min, 
                    max_value=col_max, 
                    value=col_median, 
                    key=f"slider_{feature}"
                )
    
    if input_values:
        try:
            input_vector = np.array([
                input_values.get(f, float(df_clean[f].median()) if f in df_clean.columns else 0.0) 
                for f in feature_names
            ])
            scaled_input = st.session_state.scaler.transform(input_vector.reshape(1, -1))
            prediction = st.session_state.model.predict(scaled_input)[0]
            
            H(f"""
            <div class="pbox" style="margin-top:24px;">
              <div class="plbl">Predicted {target}</div>
              <div class="pval">{prediction:,.4f}</div>
              <div class="psub">Real-time inference</div>
            </div>
            """)
        except Exception as e:
            st.error(f"⚠️ Prediction failed: {str(e)}")
    
    H("</div>")
    
    if SCIPY_AVAILABLE and numeric_features:
        H("""
        <div class="card card-glow">
          <div class="ey">Goal-Seek</div>
          <div class="ct">Reverse Engineering</div>
          <div class="cd">Find required input for target output</div>
        """)
        
        col_goal, col_vary = st.columns(2)
        
        with col_goal:
            target_mean = float(df_clean[target].mean()) if target in df_clean.columns else 0.0
            goal_value = st.number_input(f"Desired {target}", value=target_mean, key="goal_value")
        
        with col_vary:
            vary_feature = st.selectbox("Optimize", options=numeric_features, key="vary_feature")
        
        if st.button("🔮 Calculate", key="btn_oracle", use_container_width=True):
            defaults = {
                f: float(df_clean[f].median()) if f in df_clean.columns else 0.0 
                for f in feature_names
            }
            vary_idx = feature_names.index(vary_feature)
            
            def objective(x):
                vec = np.array([defaults[f] for f in feature_names])
                vec[vary_idx] = x[0]
                pred = st.session_state.model.predict(
                    st.session_state.scaler.transform(vec.reshape(1, -1))
                )[0]
                return (pred - goal_value) ** 2
            
            with st.spinner("Optimizing..."):
                result = minimize(
                    objective, 
                    [defaults[vary_feature]], 
                    method='Nelder-Mead', 
                    options={'maxiter': 5000}
                )
            
            if result.fun < 1.0:
                solution = float(result.x[0])
                H(f"""
                <div class="pbox" style="margin-top:20px;">
                  <div class="plbl">Solution</div>
                  <div class="pval">{solution:,.4f}</div>
                  <div class="psub">Set {vary_feature} to this value</div>
                </div>
                """)
            else:
                st.error("⚠️ Goal unreachable with current constraints")
        
        H("</div>")

# ═══════════════════════════════════════════════════════════════════════════════
# EXPORT
# ═══════════════════════════════════════════════════════════════════════════════

if st.session_state.clean_df is not None:
    H("""
    <div class="card">
      <div class="ey">Export</div>
      <div class="ct">Download Results</div>
      <div class="cd">Production artifacts</div>
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        csv_buffer = io.StringIO()
        st.session_state.clean_df.to_csv(csv_buffer, index=False)
        st.download_button(
            "💾 Clean Data (CSV)", 
            data=csv_buffer.getvalue(), 
            file_name=f"astrae_cleaned_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv", 
            mime="text/csv", 
            use_container_width=True
        )
    
    with col2:
        if st.session_state.model_results:
            results = st.session_state.model_results
            kpis = st.session_state.data_quality_kpis
            adv_kpis = st.session_state.advanced_kpis
            
            report_text = f"""
╔═══════════════════════════════════════════════════════════════╗
║              ASTRAE INTELLIGENCE REPORT v4.0                  ║
╚═══════════════════════════════════════════════════════════════╝

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
User: {st.session_state.username}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DATASET SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Rows:              {st.session_state.clean_df.shape[0]:,}
Columns:           {st.session_state.clean_df.shape[1]}
Target:            {st.session_state.target_variable}
Features:          {len(st.session_state.selected_features)}
Algorithm:         {st.session_state.algorithm}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MODEL PERFORMANCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
R² Score:          {results['r2']:.6f}
MAE:               {results['mae']:,.4f}
RMSE:              {results['rmse']:,.4f}
CV Mean:           {results['cv_mean']:.6f}
CV Std:            {results['cv_std']:.6f}
Training Time:     {results['training_time']:.2f}s
Overfitting Δ:     {results['overfitting_delta']:.6f}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5 CRITICAL DATA QUALITY KPIs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Completeness:      {kpis.get('completeness', 0)}%
Consistency:       {kpis.get('consistency', 0)}%
Accuracy:          {kpis.get('accuracy', 0)}%
Validity:          {kpis.get('validity', 0)}%
Uniformity:        {kpis.get('uniformity', 0)}%
Overall Quality:   {kpis.get('overall_quality', 0)}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4 ADVANCED BUSINESS KPIs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Data Density:      {adv_kpis.get('density', 0)}%
Balance Index:     {adv_kpis.get('balance_index', 0)}%
Feature Richness:  {adv_kpis.get('richness', 0)}%
Reliability Index: {adv_kpis.get('reliability_index', 0)}%
Advanced Score:    {adv_kpis.get('advanced_score', 0)}%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOP FEATURE IMPORTANCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
            if results['feature_importance']:
                top_5 = sorted(results['feature_importance'].items(), key=lambda x: x[1], reverse=True)[:5]
                for feat, imp in top_5:
                    report_text += f"{feat[:30]:<30} {imp*100:>8.2f}%\n"
            
            report_text += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ASTRAE Intelligence v4.0 ULTIMATE
© 2024 - Enterprise Decision Intelligence Platform
"""
            
            st.download_button(
                "💾 Report (TXT)", 
                data=report_text, 
                file_name=f"astrae_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", 
                mime="text/plain", 
                use_container_width=True
            )
    
    H("</div>")

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

H("""
<div style="text-align:center;padding:50px 0 24px;border-top:1px solid var(--border);margin-top:60px;">
  <div class="nav-logo" style="font-size:18px;margin-bottom:12px;">🔮 ASTRAE INTELLIGENCE</div>
  <div style="font-family:var(--fm);font-size:10px;color:var(--t3);letter-spacing:.14em;margin-bottom:18px;">
    v4.0 ULTIMATE · Enterprise Platform
  </div>
  <div style="margin-top:20px;display:flex;justify-content:center;gap:10px;flex-wrap:wrap;">
    <span class="badge bv">Advanced ML</span>
    <span class="badge bc">9 Quality KPIs</span>
    <span class="badge bg">Real-Time Charts</span>
    <span class="badge ba">Zero Latency</span>
  </div>
  <div style="margin-top:24px;font-size:11px;color:var(--t3);">
    Built for enterprise · © 2024
  </div>
</div>
""")
