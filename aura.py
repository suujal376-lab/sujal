<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <title>AURA Z · Ultimate</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
    <style>
        /* ─── CSS VARIABLES / THEMES ─── */
        :root {
            --bg-primary: #07070e;
            --bg-secondary: rgba(255,255,255,0.055);
            --bg-modal: rgba(12,14,24,0.92);
            --text-primary: #e8edf5;
            --text-dim: rgba(255,255,255,0.48);
            --text-muted: rgba(255,255,255,0.32);
            --glass-border: rgba(255,255,255,0.12);
            --accent: #c0c8d8;
            --accent-glow: rgba(180,190,210,0.2);
            --shadow: 0 8px 32px rgba(0,0,0,0.3);
            --card-bg: rgba(255,255,255,0.055);
            --green: #4ade80;
            --red: #ff6b61;
            --orange: #ffb340;
            --blue: #6b8cff;
            --transition: 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        [data-theme="silver"] {
            --bg-primary: #0e0e16;
            --text-primary: #e8ecf0;
            --accent: #d0d8e8;
            --glass-border: rgba(255,255,255,0.18);
            --bg-secondary: rgba(255,255,255,0.1);
            --card-bg: rgba(255,255,255,0.08);
        }
        [data-theme="cosmic"] {
            --bg-primary: #08041a;
            --text-primary: #e8e0f5;
            --accent: #a78bfa;
            --glass-border: rgba(167,139,250,0.2);
            --bg-secondary: rgba(167,139,250,0.06);
            --card-bg: rgba(167,139,250,0.06);
            --accent-glow: rgba(167,139,250,0.15);
            --green: #6ee7b7;
            --red: #fca5a5;
            --orange: #fcd34d;
            --blue: #93bbfc;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            overflow: hidden;
            position: relative;
            transition: background var(--transition), color var(--transition);
        }
        #starCanvas {
            position: fixed; inset: 0; z-index: 0;
            display: block; width: 100vw; height: 100vh;
        }
        ::-webkit-scrollbar { width: 5px; height: 5px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(192,200,216,0.2); border-radius: 10px; }

        /* ─── APP ─── */
        .app {
            position: relative; z-index: 2;
            display: flex; height: 100vh; padding: 12px; gap: 12px;
            animation: fadeIn 0.5s ease;
        }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        /* ─── SIDEBAR ─── */
        .sidebar {
            width: 200px;
            background: var(--bg-secondary);
            backdrop-filter: blur(32px) saturate(1.15);
            -webkit-backdrop-filter: blur(32px) saturate(1.15);
            border: 1px solid var(--glass-border);
            border-radius: 20px; padding: 18px 12px;
            display: flex; flex-direction: column; flex-shrink: 0; height: 100%;
            box-shadow: var(--shadow), inset 0 1px 0 rgba(255,255,255,0.05);
            transition: all var(--transition);
            overflow: hidden;
        }
        .sidebar.collapsed { width: 64px; padding: 18px 8px; }
        .sidebar.collapsed .logo-text,
        .sidebar.collapsed .nav-label,
        .sidebar.collapsed .footer-text { display: none; }
        .sidebar.collapsed .nav-item { justify-content: center; padding: 10px; }
        .sidebar.collapsed .logo { margin-bottom: 16px; padding-bottom: 12px; }

        .sidebar-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.06); }
        .logo { font-family: 'Orbitron', sans-serif; font-weight: 900; font-size: 17px; letter-spacing: 1.5px; cursor: pointer; user-select: none; }
        .logo-mark {
            background: linear-gradient(135deg, var(--accent), #ffffff, var(--accent));
            background-size: 200% 200%;
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: silverShift 5s ease-in-out infinite alternate;
        }
        @keyframes silverShift {
            0% { background-position: 0% 50%; }
            100% { background-position: 100% 50%; }
        }
        .hamburger {
            background: none; border: none; color: var(--text-dim); font-size: 20px;
            cursor: pointer; padding: 4px; border-radius: 8px; transition: 0.2s;
            display: none; line-height: 1;
        }
        .hamburger:hover { background: rgba(255,255,255,0.06); color: #fff; }
        .nav { flex: 1; display: flex; flex-direction: column; gap: 3px; }
        .nav-item {
            padding: 9px 12px; border-radius: 12px; font-size: 13px; font-weight: 500;
            color: var(--text-dim); cursor: pointer; transition: all 0.22s ease;
            display: flex; align-items: center; gap: 10px; border: 1px solid transparent;
        }
        .nav-item:hover { background: rgba(255,255,255,0.07); color: #fff; }
        .nav-item.active {
            background: rgba(var(--accent), 0.12); color: #e4e8f0;
            border-color: rgba(var(--accent), 0.2);
            box-shadow: 0 0 20px var(--accent-glow);
        }
        .nav-item .icon { font-size: 14px; width: 18px; text-align: center; flex-shrink: 0; }
        .footer-text {
            border-top: 1px solid rgba(255,255,255,0.06); padding-top: 12px;
            font-size: 10px; color: var(--text-muted); text-align: center; letter-spacing: 0.5px;
        }
        .footer-text span { color: var(--accent); font-weight: 500; }

        /* ─── MAIN ─── */
        .main {
            flex: 1;
            background: var(--bg-secondary);
            backdrop-filter: blur(28px) saturate(1.1);
            -webkit-backdrop-filter: blur(28px) saturate(1.1);
            border: 1px solid var(--glass-border); border-radius: 20px;
            padding: 18px 22px; overflow-y: auto; height: 100%;
            box-shadow: var(--shadow), inset 0 1px 0 rgba(255,255,255,0.04);
            animation: slideUp 0.5s ease;
            transition: background var(--transition), border var(--transition);
        }
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(12px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* ─── TOPBAR ─── */
        .topbar {
            display: flex; align-items: center; justify-content: space-between;
            flex-wrap: wrap; gap: 10px; margin-bottom: 16px; padding-bottom: 12px;
            border-bottom: 1px solid rgba(255,255,255,0.06);
        }
        .topbar-left { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
        .greeting { font-size: 15px; font-weight: 500; color: var(--text-primary); }
        .greeting span { color: var(--accent); font-weight: 400; }
        .search-wrap { position: relative; display: flex; align-items: center; }
        .search-wrap input {
            background: rgba(0,0,0,0.25); border: 1px solid rgba(255,255,255,0.08);
            color: var(--text-primary); padding: 7px 12px 7px 32px; border-radius: 40px;
            font-size: 12px; width: 150px; outline: none; transition: all 0.25s;
            font-family: 'Inter', sans-serif;
        }
        .search-wrap input:focus { border-color: rgba(var(--accent), 0.3); width: 200px; }
        .search-wrap input::placeholder { color: var(--text-muted); }
        .search-icon { position: absolute; left: 12px; font-size: 12px; color: var(--text-muted); }
        .topbar .actions { display: flex; gap: 6px; flex-wrap: wrap; align-items: center; }

        /* ─── BUTTONS ─── */
        .btn {
            font-family: 'Inter', sans-serif; font-weight: 500; font-size: 11px;
            padding: 7px 14px; border-radius: 40px;
            border: 1px solid rgba(255,255,255,0.1);
            background: rgba(255,255,255,0.05); color: rgba(255,255,255,0.7);
            cursor: pointer; transition: all 0.22s ease; backdrop-filter: blur(4px);
            white-space: nowrap;
        }
        .btn:hover { background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.2); color: #fff; transform: translateY(-1px); }
        .btn-primary { background: rgba(var(--accent), 0.15); border-color: rgba(var(--accent), 0.3); color: var(--accent); font-weight: 600; }
        .btn-primary:hover { background: rgba(var(--accent), 0.25); border-color: rgba(var(--accent), 0.5); }
        .btn-success { background: rgba(52,199,89,0.1); border-color: rgba(52,199,89,0.25); color: var(--green); }
        .btn-success:hover { background: rgba(52,199,89,0.2); border-color: rgba(52,199,89,0.4); }
        .btn-danger { background: rgba(255,69,58,0.1); border-color: rgba(255,69,58,0.25); color: var(--red); }
        .btn-danger:hover { background: rgba(255,69,58,0.2); border-color: rgba(255,69,58,0.4); }
        .btn-outline { background: transparent; border-color: rgba(255,255,255,0.08); color: rgba(255,255,255,0.4); }
        .btn-outline:hover { background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.15); color: #fff; }
        .btn-sm-icon { padding: 6px 10px; font-size: 12px; }

        /* ─── STATS ─── */
        .stats-grid {
            display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
            gap: 10px; margin-bottom: 16px;
        }
        .stat-card {
            background: var(--card-bg); backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.06); border-radius: 14px;
            padding: 12px 14px; transition: all 0.25s ease; animation: fadeUp 0.4s ease backwards;
        }
        .stat-card:nth-child(1) { animation-delay: 0.03s; }
        .stat-card:nth-child(2) { animation-delay: 0.06s; }
        .stat-card:nth-child(3) { animation-delay: 0.09s; }
        .stat-card:nth-child(4) { animation-delay: 0.12s; }
        @keyframes fadeUp { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .stat-card:hover { border-color: rgba(var(--accent), 0.2); transform: translateY(-2px); }
        .stat-card .label { font-size: 9px; text-transform: uppercase; letter-spacing: 1px; color: var(--text-muted); font-weight: 500; }
        .stat-card .number {
            font-family: 'Orbitron', sans-serif; font-weight: 700; font-size: 22px; margin-top: 2px;
            background: linear-gradient(135deg, var(--accent), #ffffff);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
        }
        .stat-card .sub { font-size: 10px; color: var(--text-muted); margin-top: 1px; }

        /* ─── FILTER BAR ─── */
        .filter-bar { display: flex; gap: 5px; margin-bottom: 12px; flex-wrap: wrap; align-items: center; }
        .filter-chip {
            font-size: 10px; font-weight: 500; padding: 4px 11px; border-radius: 40px;
            border: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.03);
            color: var(--text-dim); cursor: pointer; transition: all 0.2s;
            font-family: 'Inter', sans-serif;
        }
        .filter-chip:hover { background: rgba(255,255,255,0.06); color: #fff; }
        .filter-chip.active {
            background: rgba(var(--accent), 0.12); border-color: rgba(var(--accent), 0.25); color: var(--accent);
        }
        .filter-bar .spacer { flex: 1; }
        .theme-btn { font-size: 14px; padding: 4px 8px; border-radius: 40px; border: 1px solid transparent; background: transparent; color: var(--text-dim); cursor: pointer; transition: 0.2s; }
        .theme-btn:hover { background: rgba(255,255,255,0.05); color: #fff; }

        /* ─── CARDS ─── */
        .grid {
            display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 12px;
        }
        .card {
            background: var(--card-bg); backdrop-filter: blur(8px);
            border: 1px solid rgba(255,255,255,0.06); border-radius: 16px;
            padding: 14px 15px 12px; transition: all var(--transition);
            position: relative; box-shadow: 0 4px 16px rgba(0,0,0,0.12);
            animation: cardAppear 0.4s ease backwards;
        }
        .card:nth-child(1) { animation-delay: 0.03s; }
        .card:nth-child(2) { animation-delay: 0.06s; }
        .card:nth-child(3) { animation-delay: 0.09s; }
        .card:nth-child(4) { animation-delay: 0.12s; }
        .card:nth-child(5) { animation-delay: 0.15s; }
        .card:nth-child(6) { animation-delay: 0.18s; }
        @keyframes cardAppear { from { opacity: 0; transform: translateY(12px) scale(0.97); } to { opacity: 1; transform: translateY(0) scale(1); } }
        .card:hover { transform: translateY(-3px); border-color: rgba(var(--accent), 0.2); box-shadow: 0 12px 36px rgba(0,0,0,0.25); background: rgba(255,255,255,0.07); }
        .card.running { border-color: rgba(52,199,89,0.25); }
        .card.running::after { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 2px; background: linear-gradient(90deg, transparent, #4ade80, transparent); animation: runningBar 2.5s ease-in-out infinite; }
        @keyframes runningBar { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }
        .card.cooldown { border-color: rgba(255,159,10,0.2); }

        .card-top { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
        .status-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
        .status-dot.on { background: #4ade80; box-shadow: 0 0 10px rgba(74,222,128,0.5); animation: pulse-dot 2s infinite; }
        .status-dot.cooldown { background: #ffb340; box-shadow: 0 0 10px rgba(255,179,64,0.4); animation: pulse-dot 2s infinite; }
        .status-dot.off { background: rgba(255,255,255,0.15); }
        @keyframes pulse-dot { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.4; transform: scale(0.8); } }
        .card-name { font-weight: 560; font-size: 13px; flex: 1; color: var(--text-primary); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
        .card-time { font-size: 10px; color: var(--text-muted); font-family: 'Inter', monospace; margin-right: 4px; }
        .schedule-badge { font-size: 10px; color: var(--blue); opacity: 0.7; cursor: help; margin-left: 2px; }

        .status-pill {
            display: inline-flex; align-items: center; gap: 3px;
            font-size: 9px; font-weight: 600; padding: 2px 8px; border-radius: 40px;
            text-transform: uppercase; letter-spacing: 0.3px;
        }
        .status-pill.running { background: rgba(74,222,128,0.12); color: var(--green); border: 1px solid rgba(74,222,128,0.2); }
        .status-pill.cooldown { background: rgba(255,179,64,0.12); color: var(--orange); border: 1px solid rgba(255,179,64,0.2); }
        .status-pill.idle { background: rgba(255,255,255,0.04); color: var(--text-dim); border: 1px solid rgba(255,255,255,0.06); }

        .card-stats { display: flex; gap: 10px; font-size: 11px; color: var(--text-dim); margin: 6px 0 8px; }
        .card-stats strong { color: var(--text-primary); font-weight: 600; }
        .card-actions { display: flex; gap: 4px; flex-wrap: wrap; align-items: center; }
        .btn-sm {
            font-family: 'Inter', sans-serif; font-weight: 500; font-size: 10px;
            padding: 3px 9px; border-radius: 40px;
            border: 1px solid rgba(255,255,255,0.08); background: rgba(255,255,255,0.04);
            color: var(--text-dim); cursor: pointer; transition: all 0.2s ease;
        }
        .btn-sm:hover { background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.16); color: #fff; }
        .btn-sm-start { background: rgba(74,222,128,0.08); border-color: rgba(74,222,128,0.2); color: var(--green); }
        .btn-sm-start:hover { background: rgba(74,222,128,0.18); border-color: rgba(74,222,128,0.35); }
        .btn-sm-stop { background: rgba(255,69,58,0.08); border-color: rgba(255,69,58,0.2); color: var(--red); }
        .btn-sm-stop:hover { background: rgba(255,69,58,0.18); border-color: rgba(255,69,58,0.35); }
        .btn-sm-clone { background: rgba(107,140,255,0.06); border-color: rgba(107,140,255,0.15); color: var(--blue); }
        .btn-sm-clone:hover { background: rgba(107,140,255,0.14); border-color: rgba(107,140,255,0.3); }
        .btn-sm-del:hover { border-color: var(--red); color: var(--red); }
        .btn-sm-expand { background: transparent; border: none; color: rgba(255,255,255,0.15); font-size: 12px; cursor: pointer; padding: 2px 4px; margin-left: auto; transition: color 0.2s; }
        .btn-sm-expand:hover { color: rgba(255,255,255,0.5); }

        .card-detail {
            margin-top: 9px; padding-top: 9px; border-top: 1px solid rgba(255,255,255,0.05);
            display: none; font-size: 11px; color: var(--text-dim); animation: slideDown 0.2s ease;
        }
        @keyframes slideDown { from { opacity: 0; transform: translateY(-5px); } to { opacity: 1; transform: translateY(0); } }
        .card-detail.open { display: block; }
        .gc-pill { display: inline-block; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.06); padding: 1px 8px; border-radius: 40px; margin: 2px 3px 2px 0; font-size: 10px; color: rgba(255,255,255,0.5); }
        .detail-line { padding: 2px 0; }
        .detail-line strong { color: rgba(255,255,255,0.4); font-weight: 500; }
        .last-action-text { color: var(--accent); font-weight: 500; font-size: 10px; margin-top: 3px; }

        /* ─── LOGS ─── */
        .log-panel { display: none; margin-top: 7px; background: rgba(0,0,0,0.35); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; overflow: hidden; }
        .log-panel.open { display: block; }
        .log-header { display: flex; justify-content: space-between; padding: 4px 10px; background: rgba(0,0,0,0.2); font-size: 9px; color: var(--text-muted); border-bottom: 1px solid rgba(255,255,255,0.04); font-weight: 500; letter-spacing: 0.3px; }
        .log-live { color: var(--green); display: flex; align-items: center; gap: 4px; }
        .log-live::before { content: ''; width: 4px; height: 4px; background: #4ade80; border-radius: 50%; animation: live-pulse 1.4s infinite; }
        @keyframes live-pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.2; } }
        .log-box { height: 100px; overflow-y: auto; padding: 5px 10px; font-family: 'Inter', monospace; font-size: 10px; line-height: 1.6; color: rgba(255,255,255,0.4); }
        .log-line.ok { color: var(--green); }
        .log-line.err { color: var(--red); }
        .log-line.warn { color: var(--orange); }
        .log-line.info { color: var(--blue); }

        /* ─── ACTIVITY FEED ─── */
        .activity-panel {
            margin-top: 16px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.05);
        }
        .activity-panel .feed-title {
            font-size: 11px; font-weight: 600; color: var(--text-muted); letter-spacing: 0.5px; margin-bottom: 6px;
        }
        .feed-item {
            display: flex; align-items: center; gap: 8px;
            padding: 3px 0; font-size: 11px; color: var(--text-dim); border-bottom: 1px solid rgba(255,255,255,0.02);
        }
        .feed-item .time { font-size: 9px; color: var(--text-muted); font-family: monospace; flex-shrink: 0; }
        .feed-item .msg { flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
        .feed-item .badge { font-size: 8px; padding: 1px 6px; border-radius: 40px; background: rgba(255,255,255,0.06); color: var(--text-muted); }

        /* ─── EMPTY ─── */
        .empty { text-align: center; padding: 50px 20px; color: var(--text-dim); grid-column: 1 / -1; }
        .empty-icon { font-size: 32px; margin-bottom: 8px; opacity: 0.4; animation: floatIcon 3s ease-in-out infinite; }
        @keyframes floatIcon { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-6px); } }
        .empty-text { font-size: 13px; line-height: 1.5; }
        .empty-text .hint { display: block; margin-top: 4px; font-size: 11px; color: var(--text-muted); }

        /* ─── TOASTS ─── */
        .toast-container { position: fixed; bottom: 20px; right: 20px; z-index: 10000; display: flex; flex-direction: column; gap: 6px; pointer-events: none; }
        .toast {
            pointer-events: auto; background: rgba(16,18,28,0.9); backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.1); border-radius: 12px;
            padding: 10px 14px; min-width: 220px; max-width: 320px;
            box-shadow: 0 12px 40px rgba(0,0,0,0.4);
            display: flex; align-items: flex-start; gap: 8px;
            animation: toastIn 0.3s cubic-bezier(0.22, 1, 0.36, 1);
            font-size: 12px; color: var(--text-primary);
        }
        .toast.leaving
