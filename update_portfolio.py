import json

with open("images_b64.json", "r") as f:
    images = json.load(f)

img_fatloss = images["fatloss"]
img_muscle = images["muscle"]
img_recomp = images["recomp"]

html_template = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
  <title>Karlsthetics Fitness | Evidence-Based Online Coaching</title>
  <meta name="description" content="Science-based online fitness coaching for training, nutrition, and body composition. Custom programming adjusted weekly by a certified personal trainer, physique competitor, and physical therapy background.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;500;600;700&family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600;1,700&display=swap" rel="stylesheet">
  
  <style>
    /* CSS TOKENS & RESET */
    :root {{
      --turf: #0E2A1F;
      --moss: #1D4A35;
      --mustard: #F2B705;
      --mustard-hover: #db9f00;
      --ink: #101512;
      --chalk: #E9ECE4;
      --chalk-card: #FFFFFF;
      --chalk-border: rgba(14, 42, 31, 0.12);
      --chalk-text: #101512;
      --chalk-muted: #425248;

      /* Gradients */
      --grad-turf: linear-gradient(100deg, #F6FFE6, #C6F6A4 48%, #F2B705);
      --grad-chalk: linear-gradient(100deg, #0E2A1F 0%, #1B6A43 50%, #23784A 100%);
      --grad-mustard: linear-gradient(100deg, #101512 0%, #0E2A1F 55%, #1D4A35 100%);
      --grad-wordmark: linear-gradient(180deg, #C6F6A4 0%, #F2B705 100%);

      /* Typography */
      --font-serif: "Cormorant Garamond", Georgia, "Times New Roman", serif;
      --font-sans: "Bricolage Grotesque", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      
      /* Spacing & Shell */
      --container-max: 1200px;
      --nav-height: 72px;
      --safe-top: env(safe-area-inset-top, 0px);
      --safe-bottom: env(safe-area-inset-bottom, 0px);
    }}

    /* System dark mode guarding: :root:not([data-theme="light"]) */
    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) {{
        --chalk: #0A0E0C;
        --chalk-card: #121915;
        --chalk-border: rgba(242, 183, 5, 0.2);
        --chalk-text: #E9ECE4;
        --chalk-muted: #A3B5AA;
        --grad-chalk: linear-gradient(100deg, #F6FFE6, #C6F6A4 48%, #F2B705);
      }}
    }}

    /* Explicit dark mode attribute override */
    :root[data-theme="dark"] {{
      --chalk: #0A0E0C;
      --chalk-card: #121915;
      --chalk-border: rgba(242, 183, 5, 0.2);
      --chalk-text: #E9ECE4;
      --chalk-muted: #A3B5AA;
      --grad-chalk: linear-gradient(100deg, #F6FFE6, #C6F6A4 48%, #F2B705);
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
      color-scheme: dark light;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--turf);
      color: var(--chalk);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      overflow-x: clip;
      position: relative;
    }}

    /* Accessibility Focus & Skip Link */
    :focus-visible {{
      outline: 3px solid var(--mustard);
      outline-offset: 3px;
    }}

    .skip-link {{
      position: absolute;
      top: -100px;
      left: 1rem;
      background: var(--mustard);
      color: var(--ink);
      padding: 0.75rem 1.25rem;
      border-radius: 9999px;
      font-weight: 700;
      z-index: 10000;
      text-decoration: none;
      transition: top 0.2s ease;
    }}
    .skip-link:focus {{
      top: 1rem;
    }}

    /* Base Typography */
    h1, h2, h3, h4, .font-serif {{
      font-family: var(--font-serif);
      font-weight: 700;
      font-variant-numeric: lining-nums;
      letter-spacing: -0.025em;
      line-height: 1.1;
    }}

    /* Gradient headings with descender safety */
    .grad-turf {{
      background-image: var(--grad-turf);
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      padding-bottom: 0.12em;
      display: inline-block;
    }}
    .grad-chalk {{
      background-image: var(--grad-chalk);
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      padding-bottom: 0.12em;
      display: inline-block;
    }}
    .grad-mustard {{
      background-image: var(--grad-mustard);
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      padding-bottom: 0.12em;
      display: inline-block;
    }}

    /* Layout Containers */
    .container {{
      width: 100%;
      max-width: var(--container-max);
      margin: 0 auto;
      padding-left: clamp(1.25rem, 5vw, 3rem);
      padding-right: clamp(1.25rem, 5vw, 3rem);
    }}

    .section-pad {{
      padding-top: clamp(4.5rem, 8vw, 7.5rem);
      padding-bottom: clamp(4.5rem, 8vw, 7.5rem);
    }}

    /* Common Buttons & Chips */
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      font-family: var(--font-sans);
      font-size: 1rem;
      font-weight: 600;
      padding: 0.85rem 1.85rem;
      border-radius: 9999px;
      text-decoration: none;
      cursor: pointer;
      transition: transform 0.18s ease, background-color 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
      white-space: nowrap;
      border: 2px solid transparent;
      min-height: 48px;
    }}
    .btn:hover {{
      transform: translateY(-2px);
    }}
    .btn:active {{
      transform: translateY(0);
    }}

    .btn-primary {{
      background-color: var(--mustard);
      color: var(--ink);
      border-color: var(--mustard);
      box-shadow: 0 4px 14px rgba(242, 183, 5, 0.25);
    }}
    .btn-primary:hover {{
      background-color: #f7c32b;
      box-shadow: 0 6px 20px rgba(242, 183, 5, 0.35);
    }}

    .btn-secondary {{
      background-color: transparent;
      color: var(--chalk);
      border-color: rgba(233, 236, 228, 0.45);
    }}
    .btn-secondary:hover {{
      border-color: var(--chalk);
      background-color: rgba(233, 236, 228, 0.08);
    }}

    .btn-outline-dark {{
      background-color: transparent;
      color: var(--ink);
      border-color: rgba(16, 21, 18, 0.4);
    }}
    .btn-outline-dark:hover {{
      border-color: var(--ink);
      background-color: rgba(16, 21, 18, 0.08);
    }}

    /* Pill Filter Chips */
    .chip-group {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      align-items: center;
    }}
    .chip {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 0.55rem 1.25rem;
      border-radius: 9999px;
      border: 2px solid var(--chip-border, rgba(233, 236, 228, 0.35));
      background-color: transparent;
      color: var(--chip-text, var(--chalk));
      font-family: var(--font-sans);
      font-size: 0.925rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      min-height: 40px;
    }}
    .chip:hover {{
      border-color: var(--mustard);
    }}
    .chip[aria-pressed="true"], .chip.active {{
      background-color: var(--mustard);
      border-color: var(--mustard);
      color: var(--ink) !important;
      box-shadow: 0 3px 10px rgba(242, 183, 5, 0.25);
    }}

    /* Weight Plate Ring Icon Helper */
    .ring-plate-icon {{
      display: inline-block;
      vertical-align: middle;
      flex-shrink: 0;
    }}

    /* 1. FIXED TOP BAR */
    .header-bar {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 1000;
      height: var(--nav-height);
      padding-top: var(--safe-top);
      background-color: rgba(14, 42, 31, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(242, 183, 5, 0.15);
      transition: background-color 0.3s ease;
    }}
    .header-inner {{
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .brand-logo {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: var(--chalk);
    }}
    .brand-logo .brand-text {{
      font-family: var(--font-serif);
      font-weight: 700;
      font-size: clamp(1.2rem, 2.5vw, 1.45rem);
      letter-spacing: -0.015em;
      color: #F6FFE6;
    }}
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }}
    .header-apply {{
      font-size: 0.875rem;
      padding: 0.6rem 1.25rem;
      min-height: 40px;
    }}
    @media (max-width: 768px) {{
      .header-apply {{
        display: none;
      }}
    }}

    /* Theme Toggle */
    .theme-toggle-btn {{
      background: transparent;
      border: 1px solid rgba(233, 236, 228, 0.25);
      border-radius: 9999px;
      color: var(--chalk);
      width: 40px;
      height: 40px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .theme-toggle-btn:hover {{
      border-color: var(--mustard);
      color: var(--mustard);
    }}

    /* Menu Toggle Button */
    .menu-trigger-btn {{
      background-color: rgba(29, 74, 53, 0.6);
      border: 1.5px solid rgba(242, 183, 5, 0.4);
      color: var(--chalk);
      padding: 0.55rem 1.25rem;
      border-radius: 9999px;
      font-family: var(--font-sans);
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
    }}
    .menu-trigger-btn:hover {{
      background-color: var(--moss);
      border-color: var(--mustard);
      color: var(--mustard);
    }}

    /* 2. FULL-SCREEN MENU OVERLAY */
    .menu-overlay {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100vh;
      background-color: var(--mustard);
      color: var(--ink);
      z-index: 2000;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: clamp(1.5rem, 5vw, 3rem);
      padding-top: calc(var(--safe-top) + 1.5rem);
      padding-bottom: calc(var(--safe-bottom) + 1.5rem);
      opacity: 0;
      pointer-events: none;
      transform: translateY(-100%);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
    }}
    .menu-overlay.active {{
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0);
    }}
    .menu-overlay-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
    }}
    .menu-overlay-close {{
      background: transparent;
      border: 2px solid var(--ink);
      color: var(--ink);
      border-radius: 9999px;
      padding: 0.55rem 1.4rem;
      font-family: var(--font-sans);
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s ease;
    }}
    .menu-overlay-close:hover {{
      background-color: var(--ink);
      color: var(--mustard);
    }}
    .menu-nav-links {{
      display: flex;
      flex-direction: column;
      gap: clamp(0.5rem, 2.5vw, 1.25rem);
      margin: auto 0;
    }}
    .menu-link-item {{
      text-decoration: none;
      font-family: var(--font-serif);
      font-size: clamp(2.5rem, 7.5vw, 5.25rem);
      font-weight: 700;
      color: var(--ink);
      line-height: 1.05;
      letter-spacing: -0.03em;
      transition: opacity 0.25s ease, transform 0.25s ease;
      display: inline-block;
      width: fit-content;
    }}
    .menu-nav-links:hover .menu-link-item {{
      opacity: 0.35;
    }}
    .menu-nav-links .menu-link-item:hover,
    .menu-nav-links .menu-link-item:focus {{
      opacity: 1;
      transform: translateX(16px);
    }}
    .menu-overlay-footer {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      border-top: 1.5px solid rgba(16, 21, 18, 0.2);
      padding-top: 1.25rem;
    }}
    .menu-footer-text {{
      font-size: clamp(0.95rem, 1.8vw, 1.15rem);
      font-weight: 500;
      color: var(--ink);
      max-width: 540px;
    }}
    .menu-social-links {{
      display: flex;
      gap: 0.75rem;
      align-items: center;
    }}

    /* 3. HERO (dark turf, no photo) */
    .hero-section {{
      background-color: var(--turf);
      padding-top: calc(var(--nav-height) + clamp(3.5rem, 9vw, 7rem));
      padding-bottom: clamp(4rem, 9vw, 8rem);
      position: relative;
      overflow: hidden;
    }}
    .hero-container {{
      max-width: var(--container-max);
    }}
    .hero-headline {{
      font-size: clamp(2.75rem, 8.5vw, 6.5rem);
      font-weight: 700;
      line-height: 1.02;
      margin-bottom: clamp(1.5rem, 3.5vw, 2.5rem);
      display: flex;
      flex-direction: column;
    }}
    .hero-line-mask {{
      overflow: hidden;
      display: block;
      padding-bottom: 0.1em;
    }}
    .hero-line {{
      display: block;
      transform: translateY(115%);
      animation: revealUp 0.85s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      background-image: var(--grad-turf);
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .hero-line-1 {{ animation-delay: 0.1s; }}
    .hero-line-2 {{ animation-delay: 0.22s; }}
    .hero-line-3 {{ animation-delay: 0.34s; }}

    @keyframes revealUp {{
      0% {{ transform: translateY(115%); opacity: 0; }}
      100% {{ transform: translateY(0%); opacity: 1; }}
    }}

    .hero-copy {{
      font-size: clamp(1.1rem, 2.2vw, 1.35rem);
      max-width: 740px;
      color: rgba(233, 236, 228, 0.88);
      margin-bottom: clamp(2rem, 4vw, 3rem);
      line-height: 1.65;
      opacity: 0;
      animation: fadeInHero 0.8s ease forwards;
      animation-delay: 0.55s;
    }}

    .hero-ctas {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      align-items: center;
      opacity: 0;
      animation: fadeInHero 0.8s ease forwards;
      animation-delay: 0.7s;
    }}

    /* Trust Badges in Hero */
    .hero-trust-bar {{
      margin-top: 2.5rem;
      display: flex;
      flex-wrap: wrap;
      gap: 1.25rem;
      align-items: center;
      opacity: 0;
      animation: fadeInHero 0.8s ease forwards;
      animation-delay: 0.85s;
    }}
    .trust-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.88rem;
      font-weight: 600;
      color: rgba(246, 255, 230, 0.85);
      background: rgba(29, 74, 53, 0.5);
      border: 1px solid rgba(242, 183, 5, 0.25);
      padding: 0.4rem 0.9rem;
      border-radius: 9999px;
    }}
    .trust-badge svg {{
      color: var(--mustard);
    }}

    @keyframes fadeInHero {{
      0% {{ opacity: 0; transform: translateY(12px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}

    /* 4. TICKER (mustard band) */
    .ticker-band {{
      background-color: var(--mustard);
      color: var(--ink);
      overflow: hidden;
      white-space: nowrap;
      padding: 1.15rem 0;
      border-top: 2px solid var(--ink);
      border-bottom: 2px solid var(--ink);
      user-select: none;
      display: flex;
    }}
    .ticker-track {{
      display: flex;
      align-items: center;
      flex-shrink: 0;
      animation: tickerMarquee 32s linear infinite;
    }}
    .ticker-band:hover .ticker-track {{
      animation-play-state: paused;
    }}
    .ticker-item {{
      font-family: var(--font-serif);
      font-weight: 700;
      font-size: clamp(1.25rem, 2.4vw, 1.85rem);
      letter-spacing: -0.02em;
      display: inline-flex;
      align-items: center;
      gap: 1.5rem;
      padding: 0 1.5rem;
    }}
    @keyframes tickerMarquee {{
      0% {{ transform: translateX(0); }}
      100% {{ transform: translateX(-100%); }}
    }}

    /* 5. ONLINE COACHING (chalk background - main section) */
    .coaching-section {{
      background-color: var(--chalk);
      color: var(--chalk-text);
      transition: background-color 0.3s ease, color 0.3s ease;
    }}
    .statement-banner {{
      margin-bottom: clamp(2.5rem, 5vw, 4rem);
    }}
    .statement-sentence {{
      font-family: var(--font-serif);
      font-size: clamp(2rem, 5vw, 4.25rem);
      font-weight: 700;
      line-height: 1.12;
      color: var(--chalk-text);
      letter-spacing: -0.025em;
    }}
    .statement-pill {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background-color: var(--mustard);
      color: var(--ink);
      padding: 0.15em 0.55em;
      border-radius: 9999px;
      vertical-align: middle;
      margin: 0 0.2em;
      box-shadow: 0 2px 8px rgba(242, 183, 5, 0.3);
    }}
    .statement-pill svg {{
      width: clamp(1.2rem, 3vw, 2.2rem);
      height: clamp(1.2rem, 3vw, 2.2rem);
    }}

    .lede-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: clamp(1.5rem, 4vw, 3.5rem);
      margin-bottom: clamp(3.5rem, 7vw, 5.5rem);
    }}
    @media (max-width: 768px) {{
      .lede-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .lede-p {{
      font-size: clamp(1.05rem, 1.8vw, 1.25rem);
      line-height: 1.7;
      color: var(--chalk-muted);
    }}
    .lede-p strong {{
      color: var(--chalk-text);
    }}

    /* "How it works" Accessible Tabs Widget */
    .tabs-wrapper {{
      background-color: var(--chalk-card);
      border-radius: 24px;
      border: 1px solid var(--chalk-border);
      padding: clamp(1.5rem, 4vw, 3rem);
      box-shadow: 0 10px 30px rgba(0,0,0,0.06);
      margin-bottom: clamp(3.5rem, 6vw, 5rem);
    }}
    .tabs-heading-row {{
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      margin-bottom: 2rem;
      border-bottom: 1px solid var(--chalk-border);
      padding-bottom: 1rem;
    }}
    .tabs-heading {{
      font-size: clamp(1.75rem, 3.5vw, 2.75rem);
    }}
    .tabs-layout {{
      display: grid;
      grid-template-columns: 340px 1fr;
      gap: clamp(1.5rem, 4vw, 3.5rem);
      align-items: start;
    }}
    @media (max-width: 900px) {{
      .tabs-layout {{
        grid-template-columns: 1fr;
      }}
    }}

    .tab-list {{
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }}
    @media (max-width: 900px) {{
      .tab-list {{
        flex-direction: row;
        overflow-x: auto;
        padding-bottom: 0.75rem;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: thin;
      }}
    }}
    .tab-btn {{
      display: flex;
      align-items: center;
      gap: 1rem;
      padding: 1rem 1.25rem;
      border-radius: 16px;
      background: transparent;
      border: 1.5px solid transparent;
      font-family: var(--font-sans);
      font-size: 1rem;
      font-weight: 600;
      color: var(--chalk-muted);
      cursor: pointer;
      text-align: left;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}
    .tab-btn:hover {{
      background-color: rgba(14, 42, 31, 0.05);
      color: var(--chalk-text);
    }}
    .tab-btn[aria-selected="true"] {{
      background-color: var(--turf);
      color: #F6FFE6;
      border-color: var(--turf);
      box-shadow: 0 4px 16px rgba(14, 42, 31, 0.2);
    }}
    :root[data-theme="dark"] .tab-btn[aria-selected="true"],
    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) .tab-btn[aria-selected="true"] {{
        background-color: #1D4A35;
        border-color: var(--mustard);
        color: #F6FFE6;
      }}
    }}
    .tab-num {{
      font-family: var(--font-serif);
      font-size: 1.35rem;
      font-weight: 700;
      width: 28px;
      height: 28px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 9999px;
      background: rgba(242, 183, 5, 0.2);
      color: var(--mustard);
      flex-shrink: 0;
    }}
    .tab-btn[aria-selected="true"] .tab-num {{
      background: var(--mustard);
      color: var(--ink);
    }}

    .tab-panel-container {{
      position: relative;
      min-height: 280px;
    }}
    .tab-panel {{
      display: none;
      animation: panelFadeIn 0.3s ease forwards;
    }}
    .tab-panel.active {{
      display: block;
    }}
    @keyframes panelFadeIn {{
      0% {{ opacity: 0; transform: translateY(8px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}
    .tab-panel-title {{
      font-size: clamp(1.5rem, 2.8vw, 2.25rem);
      margin-bottom: 1rem;
      color: var(--chalk-text);
    }}
    .tab-panel-desc {{
      font-size: 1.1rem;
      color: var(--chalk-muted);
      line-height: 1.7;
      margin-bottom: 2rem;
    }}
    .exchange-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }}
    @media (max-width: 600px) {{
      .exchange-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .exchange-col {{
      background: rgba(14, 42, 31, 0.04);
      border: 1px solid var(--chalk-border);
      border-radius: 16px;
      padding: 1.25rem 1.5rem;
    }}
    :root[data-theme="dark"] .exchange-col,
    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) .exchange-col {{
        background: rgba(255, 255, 255, 0.03);
      }}
    }}
    .exchange-col-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--chalk-text);
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
    }}
    .exchange-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }}
    .exchange-list li {{
      font-size: 0.95rem;
      color: var(--chalk-muted);
      display: flex;
      align-items: baseline;
      gap: 0.5rem;
    }}
    .exchange-list li::before {{
      content: "•";
      color: var(--mustard);
      font-size: 1.3rem;
      line-height: 1;
    }}

    /* Enticing Comparison: The Coaching Difference */
    .difference-card {{
      background: var(--chalk-card);
      border: 1.5px solid var(--chalk-border);
      border-radius: 28px;
      padding: clamp(1.75rem, 4.5vw, 3rem);
      margin-bottom: clamp(3.5rem, 6vw, 5rem);
      box-shadow: 0 14px 36px rgba(0, 0, 0, 0.07);
      position: relative;
      overflow: hidden;
    }}
    .diff-header {{
      text-align: center;
      max-width: 780px;
      margin: 0 auto clamp(2rem, 4vw, 3rem) auto;
    }}
    .diff-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: rgba(242, 183, 5, 0.18);
      color: var(--turf);
      border: 1px solid rgba(242, 183, 5, 0.4);
      font-size: 0.88rem;
      font-weight: 700;
      padding: 0.35rem 1rem;
      border-radius: 9999px;
      margin-bottom: 1rem;
    }}
    :root[data-theme="dark"] .diff-badge,
    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) .diff-badge {{
        color: var(--mustard);
      }}
    }}
    .diff-title {{
      font-size: clamp(1.85rem, 3.8vw, 3rem);
      margin-bottom: 0.75rem;
      color: var(--chalk-text);
    }}
    .diff-subtitle {{
      font-size: clamp(1rem, 1.8vw, 1.2rem);
      color: var(--chalk-muted);
      line-height: 1.6;
    }}

    .diff-matrix-grid {{
      display: grid;
      grid-template-columns: 1fr 1.1fr;
      gap: 1.75rem;
      margin-bottom: 2.5rem;
    }}
    @media (max-width: 860px) {{
      .diff-matrix-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .diff-col {{
      border-radius: 20px;
      padding: clamp(1.25rem, 3vw, 2rem);
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }}
    .diff-col-generic {{
      background: rgba(16, 21, 18, 0.04);
      border: 1.5px dashed rgba(16, 21, 18, 0.18);
    }}
    :root[data-theme="dark"] .diff-col-generic,
    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) .diff-col-generic {{
        background: rgba(255, 255, 255, 0.02);
        border-color: rgba(255, 255, 255, 0.12);
      }}
    }}
    .diff-col-coach {{
      background: linear-gradient(145deg, rgba(14, 42, 31, 0.08) 0%, rgba(29, 74, 53, 0.12) 100%);
      border: 2px solid var(--mustard);
      box-shadow: 0 8px 24px rgba(242, 183, 5, 0.12);
      position: relative;
    }}
    :root[data-theme="dark"] .diff-col-coach,
    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) .diff-col-coach {{
        background: linear-gradient(145deg, rgba(29, 74, 53, 0.25) 0%, rgba(14, 42, 31, 0.4) 100%);
      }}
    }}
    .diff-col-title-wrap {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--chalk-border);
      padding-bottom: 0.85rem;
    }}
    .diff-col-title {{
      font-family: var(--font-serif);
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--chalk-text);
    }}
    .diff-col-tag {{
      font-size: 0.78rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
    }}
    .tag-stale {{
      background: rgba(16, 21, 18, 0.1);
      color: var(--chalk-muted);
    }}
    .tag-premium {{
      background: var(--mustard);
      color: var(--ink);
    }}

    .diff-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 1.15rem;
    }}
    .diff-item {{
      display: flex;
      align-items: flex-start;
      gap: 0.85rem;
    }}
    .diff-icon {{
      width: 24px;
      height: 24px;
      border-radius: 9999px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 0.15rem;
      font-weight: 700;
      font-size: 0.85rem;
    }}
    .diff-icon-cross {{
      background: rgba(220, 53, 69, 0.15);
      color: #c92a2a;
    }}
    .diff-icon-check {{
      background: var(--mustard);
      color: var(--ink);
    }}
    .diff-text {{
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }}
    .diff-text-headline {{
      font-size: 1rem;
      font-weight: 700;
      color: var(--chalk-text);
    }}
    .diff-text-desc {{
      font-size: 0.92rem;
      color: var(--chalk-muted);
      line-height: 1.5;
    }}

    .diff-footer-cta {{
      background: rgba(14, 42, 31, 0.05);
      border-radius: 18px;
      padding: 1.5rem clamp(1.25rem, 3vw, 2rem);
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1.25rem;
      border: 1px solid var(--chalk-border);
    }}
    :root[data-theme="dark"] .diff-footer-cta,
    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) .diff-footer-cta {{
        background: rgba(255, 255, 255, 0.03);
      }}
    }}
    .diff-footer-msg {{
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--chalk-text);
      max-width: 650px;
    }}

    /* "A sample week" widget */
    .sample-week-wrapper {{
      border-top: 1px solid var(--chalk-border);
      padding-top: clamp(2.5rem, 5vw, 4rem);
    }}
    .sample-week-header {{
      margin-bottom: 1.5rem;
    }}
    .sample-week-title {{
      font-size: clamp(1.75rem, 3.5vw, 2.5rem);
      margin-bottom: 0.5rem;
    }}
    .sample-week-caption {{
      font-size: 0.95rem;
      color: var(--chalk-muted);
    }}
    .day-buttons-scroll {{
      display: flex;
      gap: 0.65rem;
      overflow-x: auto;
      padding: 0.5rem 0 1rem 0;
      -webkit-overflow-scrolling: touch;
      scrollbar-width: thin;
    }}
    .day-btn {{
      flex: 1 0 130px;
      background: var(--chalk-card);
      border: 2px solid var(--chalk-border);
      border-radius: 16px;
      padding: 0.9rem 0.75rem;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s ease;
      font-family: var(--font-sans);
    }}
    .day-btn:hover {{
      border-color: var(--mustard);
      transform: translateY(-2px);
    }}
    .day-btn[aria-pressed="true"] {{
      background: var(--turf);
      border-color: var(--mustard);
      color: #F6FFE6;
      box-shadow: 0 4px 14px rgba(14, 42, 31, 0.25);
    }}
    :root[data-theme="dark"] .day-btn[aria-pressed="true"],
    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) .day-btn[aria-pressed="true"] {{
        background: #1D4A35;
        border-color: var(--mustard);
      }}
    }}
    .day-name {{
      display: block;
      font-family: var(--font-serif);
      font-size: 1.25rem;
      font-weight: 700;
      margin-bottom: 0.25rem;
    }}
    .day-focus {{
      display: block;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--chalk-muted);
    }}
    .day-btn[aria-pressed="true"] .day-focus {{
      color: var(--mustard);
    }}

    .day-detail-box {{
      margin-top: 1rem;
      background: var(--chalk-card);
      border: 1.5px solid var(--mustard);
      border-radius: 16px;
      padding: 1.25rem 1.75rem;
      display: flex;
      align-items: center;
      gap: 1rem;
    }}
    .day-detail-text {{
      font-size: 1.05rem;
      font-weight: 500;
      color: var(--chalk-text);
    }}

    /* 6. CLIENT HIGHLIGHTS (dark turf) */
    .highlights-section {{
      background-color: var(--turf);
      color: var(--chalk);
      position: relative;
    }}
    .highlights-header {{
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin-bottom: 2rem;
    }}
    .highlights-title {{
      font-size: clamp(2.25rem, 5.5vw, 4.5rem);
    }}
    .highlights-subtext {{
      font-size: clamp(1.05rem, 2vw, 1.25rem);
      color: rgba(233, 236, 228, 0.85);
      max-width: 680px;
    }}

    .highlights-controls-row {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 1.5rem;
      margin-bottom: 2.5rem;
    }}
    .carousel-nav-controls {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}
    .carousel-counter {{
      font-family: var(--font-serif);
      font-size: 1.35rem;
      font-weight: 700;
      letter-spacing: -0.01em;
      color: var(--mustard);
      min-width: 55px;
      text-align: center;
    }}
    .carousel-round-btn {{
      width: 46px;
      height: 46px;
      border-radius: 9999px;
      background: rgba(29, 74, 53, 0.7);
      border: 1.5px solid rgba(242, 183, 5, 0.4);
      color: var(--chalk);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }}
    .carousel-round-btn:hover:not(:disabled) {{
      background: var(--mustard);
      color: var(--ink);
      border-color: var(--mustard);
      transform: scale(1.06);
    }}
    .carousel-round-btn:disabled {{
      opacity: 0.35;
      cursor: not-allowed;
    }}

    /* Full-bleed scroll-snap carousel */
    .carousel-viewport {{
      width: 100%;
      overflow-x: auto;
      scroll-snap-type: x mandatory;
      scrollbar-width: none;
      -webkit-overflow-scrolling: touch;
      cursor: grab;
      user-select: none;
      padding: 0.5rem 0 2rem 0;
    }}
    .carousel-viewport::-webkit-scrollbar {{
      display: none;
    }}
    .carousel-viewport.is-dragging {{
      cursor: grabbing;
      scroll-behavior: auto;
      scroll-snap-type: none;
    }}
    .carousel-track {{
      display: flex;
      gap: clamp(1.25rem, 3vw, 2.5rem);
      width: max-content;
      padding-left: clamp(1.25rem, 5vw, 3rem);
      padding-right: clamp(1.25rem, 5vw, 3rem);
    }}

    .highlight-card {{
      scroll-snap-align: start;
      flex: 0 0 clamp(300px, 42vw, 480px);
      background: rgba(29, 74, 53, 0.4);
      border: 1px solid rgba(242, 183, 5, 0.2);
      border-radius: 24px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }}
    .highlight-card:hover {{
      transform: translateY(-4px);
      border-color: rgba(242, 183, 5, 0.5);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35);
    }}
    .highlight-card.hidden {{
      display: none;
    }}

    .card-photo-wrapper {{
      position: relative;
      width: 100%;
      aspect-ratio: 15 / 16;
      background: #081610;
      cursor: zoom-in;
      overflow: hidden;
    }}
    .card-photo {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      transition: transform 0.4s ease;
      display: block;
    }}
    .highlight-card:hover .card-photo {{
      transform: scale(1.025);
    }}
    .gold-tag-pill {{
      position: absolute;
      top: 1rem;
      left: 1rem;
      background-color: var(--mustard);
      color: var(--ink);
      font-family: var(--font-serif);
      font-size: 1.15rem;
      font-weight: 700;
      padding: 0.35rem 0.9rem;
      border-radius: 9999px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
      z-index: 2;
      letter-spacing: -0.01em;
    }}
    .card-zoom-badge {{
      position: absolute;
      bottom: 1rem;
      right: 1rem;
      background: rgba(14, 42, 31, 0.85);
      color: var(--chalk);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      backdrop-filter: blur(8px);
      border: 1px solid rgba(242, 183, 5, 0.3);
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }}
    .card-content {{
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }}
    .card-category {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--mustard);
      text-transform: none;
    }}
    .card-caption {{
      font-size: 1.05rem;
      color: rgba(233, 236, 228, 0.92);
      line-height: 1.55;
    }}

    .highlights-fine-print {{
      margin-top: 1.5rem;
      font-size: 0.9rem;
      color: rgba(233, 236, 228, 0.65);
      line-height: 1.5;
    }}

    /* Lightbox Dialog */
    .lightbox-dialog {{
      border: 1px solid var(--mustard);
      border-radius: 20px;
      background: #081610;
      color: var(--chalk);
      padding: 0;
      max-width: 90vw;
      max-height: 90vh;
      margin: auto;
      box-shadow: 0 20px 60px rgba(0,0,0,0.8);
      overflow: hidden;
    }}
    .lightbox-dialog::backdrop {{
      background: rgba(14, 42, 31, 0.85);
      backdrop-filter: blur(12px);
    }}
    .lightbox-inner {{
      display: flex;
      flex-direction: column;
      max-height: 90vh;
    }}
    .lightbox-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 1.5rem;
      background: #0E2A1F;
      border-bottom: 1px solid rgba(242, 183, 5, 0.2);
    }}
    .lightbox-title {{
      font-family: var(--font-serif);
      font-size: 1.35rem;
      color: var(--mustard);
    }}
    .lightbox-close {{
      background: transparent;
      border: 1px solid rgba(233, 236, 228, 0.3);
      color: var(--chalk);
      border-radius: 9999px;
      padding: 0.4rem 1rem;
      font-family: var(--font-sans);
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .lightbox-close:hover {{
      background: var(--mustard);
      color: var(--ink);
      border-color: var(--mustard);
    }}
    .lightbox-img-wrapper {{
      padding: 1rem;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: auto;
      background: #0A0E0C;
    }}
    .lightbox-img {{
      max-width: 100%;
      max-height: 65vh;
      object-fit: contain;
      border-radius: 8px;
    }}
    .lightbox-caption {{
      padding: 1rem 1.5rem;
      background: #0E2A1F;
      font-size: 1rem;
      border-top: 1px solid rgba(242, 183, 5, 0.2);
      color: rgba(233, 236, 228, 0.9);
    }}

    /* 7. CREDENTIALS (chalk) */
    .credentials-section {{
      background-color: var(--chalk);
      color: var(--chalk-text);
      transition: background-color 0.3s ease, color 0.3s ease;
    }}
    .credentials-header {{
      margin-bottom: 2rem;
    }}
    .credentials-title {{
      font-size: clamp(2.25rem, 5.5vw, 4.5rem);
      margin-bottom: 0.75rem;
    }}
    .credentials-lede {{
      font-size: clamp(1.05rem, 2vw, 1.25rem);
      color: var(--chalk-muted);
      max-width: 680px;
    }}
    .credentials-chips {{
      margin-bottom: 2.5rem;
      --chip-border: rgba(14, 42, 31, 0.2);
      --chip-text: var(--chalk-text);
    }}

    .accordion-list {{
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin-bottom: 2.5rem;
    }}
    .accordion-item {{
      background: var(--chalk-card);
      border: 1px solid var(--chalk-border);
      border-radius: 20px;
      overflow: hidden;
      transition: all 0.25s ease;
    }}
    .accordion-item:hover {{
      border-color: var(--mustard);
    }}
    .accordion-item.hidden {{
      display: none;
    }}
    .accordion-btn {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.5rem clamp(1.25rem, 3vw, 2rem);
      background: transparent;
      border: none;
      cursor: pointer;
      text-align: left;
      font-family: var(--font-serif);
      font-size: clamp(1.4rem, 2.8vw, 2.15rem);
      font-weight: 700;
      color: var(--chalk-text);
      letter-spacing: -0.02em;
    }}
    .accordion-title-wrap {{
      display: flex;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }}
    .accordion-tags {{
      display: inline-flex;
      gap: 0.4rem;
    }}
    .acc-tag {{
      font-family: var(--font-sans);
      font-size: 0.78rem;
      font-weight: 600;
      background: rgba(14, 42, 31, 0.08);
      color: var(--chalk-muted);
      padding: 0.2rem 0.65rem;
      border-radius: 9999px;
    }}
    :root[data-theme="dark"] .acc-tag,
    @media (prefers-color-scheme: dark) {{
      :root:not([data-theme="light"]) .acc-tag {{
        background: rgba(255, 255, 255, 0.08);
        color: var(--chalk-muted);
      }}
    }}
    .accordion-icon {{
      width: 38px;
      height: 38px;
      border-radius: 9999px;
      background: rgba(14, 42, 31, 0.05);
      border: 1.5px solid var(--chalk-border);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      color: var(--chalk-text);
      transition: transform 0.3s ease, background 0.2s;
    }}
    .accordion-btn[aria-expanded="true"] .accordion-icon {{
      transform: rotate(45deg);
      background: var(--mustard);
      color: var(--ink);
      border-color: var(--mustard);
    }}
    .accordion-collapse {{
      display: grid;
      grid-template-rows: 0fr;
      transition: grid-template-rows 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .accordion-collapse.open {{
      grid-template-rows: 1fr;
    }}
    .accordion-body {{
      overflow: hidden;
    }}
    .accordion-content {{
      padding: 0 clamp(1.25rem, 3vw, 2rem) 1.75rem clamp(1.25rem, 3vw, 2rem);
      font-size: 1.1rem;
      line-height: 1.7;
      color: var(--chalk-muted);
    }}
    .credentials-disclaimer {{
      font-size: 0.95rem;
      color: var(--chalk-muted);
      padding: 1.25rem 1.5rem;
      border-radius: 14px;
      border-left: 3px solid var(--mustard);
      background: var(--chalk-card);
      line-height: 1.6;
    }}

    /* 8. APPLY (full mustard block) */
    .apply-section {{
      background-color: var(--mustard);
      color: var(--ink);
      position: relative;
    }}
    .apply-header {{
      margin-bottom: clamp(2rem, 4vw, 3rem);
    }}
    .apply-title {{
      font-size: clamp(2.25rem, 5.5vw, 4.5rem);
      color: var(--ink);
      margin-bottom: 0.75rem;
    }}
    .apply-lede {{
      font-size: clamp(1.05rem, 2vw, 1.25rem);
      color: #243028;
      max-width: 680px;
    }}

    .apply-grid {{
      display: grid;
      grid-template-columns: 1.1fr 1fr;
      gap: clamp(2rem, 5vw, 4rem);
      align-items: start;
    }}
    @media (max-width: 900px) {{
      .apply-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .builder-card {{
      background: #FFE885;
      border: 2px solid var(--ink);
      border-radius: 24px;
      padding: clamp(1.5rem, 4vw, 2.5rem);
      box-shadow: 6px 6px 0px var(--ink);
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }}
    .builder-field {{
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }}
    .builder-label {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--ink);
    }}
    .builder-input {{
      width: 100%;
      padding: 0.85rem 1.2rem;
      border-radius: 12px;
      border: 2px solid var(--ink);
      background: #FFFFFF;
      font-family: var(--font-sans);
      font-size: 1rem;
      color: var(--ink);
      transition: border-color 0.2s;
    }}
    .builder-input:focus {{
      outline: none;
      border-color: var(--turf);
      box-shadow: 0 0 0 3px rgba(14, 42, 31, 0.2);
    }}
    .builder-chips {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }}
    .b-chip {{
      padding: 0.5rem 1.1rem;
      border-radius: 9999px;
      border: 2px solid var(--ink);
      background: #FFFFFF;
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .b-chip:hover {{
      background: #FFF2B2;
    }}
    .b-chip[aria-pressed="true"] {{
      background: var(--ink);
      color: var(--mustard);
      border-color: var(--ink);
    }}

    /* Message Preview Card */
    .preview-card {{
      background: #FFFFFF;
      border: 2px solid var(--ink);
      border-radius: 24px;
      padding: clamp(1.5rem, 4vw, 2.5rem);
      box-shadow: 6px 6px 0px var(--ink);
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }}
    .preview-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .preview-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--ink);
    }}
    .preview-textarea {{
      width: 100%;
      min-height: 220px;
      padding: 1.25rem;
      border-radius: 16px;
      border: 2px solid rgba(16, 21, 18, 0.2);
      background: #F8FAF6;
      font-family: var(--font-sans);
      font-size: 0.98rem;
      line-height: 1.6;
      color: var(--ink);
      resize: vertical;
    }}
    .preview-actions {{
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }}
    .btn-copy {{
      background: var(--ink);
      color: var(--mustard);
      border-color: var(--ink);
      font-size: 1.05rem;
      width: 100%;
    }}
    .btn-copy:hover {{
      background: var(--turf);
      border-color: var(--turf);
      color: #C6F6A4;
    }}
    .copy-status {{
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--turf);
      min-height: 1.4rem;
      text-align: center;
    }}

    /* Dedicated Social Media Section directly inside the White Box */
    .contact-channels {{
      border-top: 1.5px dashed rgba(16, 21, 18, 0.25);
      padding-top: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }}
    .contact-channels-label {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--ink);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .social-buttons-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
    }}
    @media (max-width: 520px) {{
      .social-buttons-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .social-action-btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.65rem;
      padding: 0.85rem 1.15rem;
      border-radius: 14px;
      font-family: var(--font-sans);
      font-size: 0.95rem;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.12);
      border: 1.5px solid transparent;
    }}
    .social-action-btn:hover {{
      transform: translateY(-2px);
      box-shadow: 0 7px 18px rgba(0, 0, 0, 0.18);
    }}
    .instagram-btn {{
      background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
      color: #FFFFFF !important;
    }}
    .instagram-btn:hover {{
      filter: brightness(1.08);
    }}
    .facebook-btn {{
      background-color: #1877F2;
      color: #FFFFFF !important;
    }}
    .facebook-btn:hover {{
      background-color: #0b67e3;
    }}
    .social-sub-note {{
      font-size: 0.82rem;
      color: #3b4c40;
      line-height: 1.45;
      margin-top: 0.2rem;
    }}

    /* 9. FOOTER (turf) */
    .footer-section {{
      background-color: var(--turf);
      color: var(--chalk);
      padding-top: clamp(4.5rem, 8vw, 7.5rem);
      padding-bottom: calc(var(--safe-bottom) + 3rem);
      border-top: 1px solid rgba(242, 183, 5, 0.2);
      position: relative;
    }}
    .footer-cta-row {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 2rem;
      margin-bottom: clamp(3.5rem, 7vw, 6rem);
      padding-bottom: 3rem;
      border-bottom: 1px solid rgba(233, 236, 228, 0.12);
    }}
    .footer-headline {{
      font-size: clamp(2rem, 4.5vw, 3.5rem);
      max-width: 500px;
    }}
    .footer-nav-list {{
      display: flex;
      flex-wrap: wrap;
      gap: clamp(1rem, 2.5vw, 2rem);
      list-style: none;
      align-items: center;
    }}
    .footer-nav-list a {{
      color: var(--chalk);
      text-decoration: none;
      font-weight: 600;
      font-size: 1.05rem;
      transition: color 0.2s;
    }}
    .footer-nav-list a:hover {{
      color: var(--mustard);
    }}

    .footer-social-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.45rem 1rem;
      border-radius: 9999px;
      background: rgba(29, 74, 53, 0.7);
      border: 1px solid rgba(242, 183, 5, 0.3);
      color: #F6FFE6 !important;
      font-size: 0.9rem !important;
      transition: all 0.2s ease;
    }}
    .footer-social-pill:hover {{
      background: var(--mustard);
      color: var(--ink) !important;
      border-color: var(--mustard);
    }}

    /* GIANT TWO-ROW WORDMARK */
    .wordmark-container {{
      width: 100%;
      overflow: hidden;
      margin-bottom: clamp(3rem, 6vw, 5rem);
      user-select: none;
    }}
    .wordmark-row {{
      display: block;
      width: 100%;
      line-height: 0.88;
      font-family: var(--font-serif);
      font-weight: 700;
      letter-spacing: -0.03em;
      white-space: nowrap;
    }}
    .wordmark-row-1 {{
      text-align: left;
    }}
    .wordmark-row-2 {{
      text-align: right;
    }}

    .roll-letter {{
      display: inline-block;
      position: relative;
      overflow: hidden;
      cursor: pointer;
      vertical-align: top;
      height: 1.05em;
    }}
    .roll-letter-inner {{
      display: inline-flex;
      flex-direction: column;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .roll-letter:hover .roll-letter-inner,
    .roll-letter.toggled .roll-letter-inner {{
      transform: translateY(-50%);
    }}
    .roll-glyph {{
      display: block;
      height: 1.05em;
      line-height: 1.05;
      background-image: var(--grad-wordmark);
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .roll-glyph.glyph-alt {{
      background-image: linear-gradient(180deg, #F2B705 0%, #FFF3B8 100%);
    }}

    .footer-legal-bar {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 1.5rem;
      font-size: 0.9rem;
      color: rgba(233, 236, 228, 0.65);
    }}
    .footer-legal-bar a {{
      color: rgba(233, 236, 228, 0.8);
      text-decoration: underline;
    }}

    /* Floating Quick Bar */
    .floating-action-pill {{
      position: fixed;
      bottom: clamp(1rem, 3vw, 2rem);
      right: clamp(1rem, 3vw, 2rem);
      z-index: 999;
      background: var(--mustard);
      color: var(--ink);
      font-family: var(--font-sans);
      font-weight: 700;
      font-size: 0.95rem;
      padding: 0.75rem 1.4rem;
      border-radius: 9999px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
      border: 2px solid var(--ink);
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      text-decoration: none;
      transform: translateY(120px);
      opacity: 0;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .floating-action-pill.visible {{
      transform: translateY(0);
      opacity: 1;
    }}
    .floating-action-pill:hover {{
      transform: translateY(-3px);
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.45);
      background: #f7c32b;
    }}

    /* Motion preference */
    @media (prefers-reduced-motion: reduce) {{
      *, *::before, *::after {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }}
      .ticker-track {{
        animation: none !important;
      }}
      .hero-line {{
        transform: none !important;
        opacity: 1 !important;
      }}
      .hero-copy, .hero-ctas, .hero-trust-bar {{
        opacity: 1 !important;
        transform: none !important;
      }}
      .roll-letter:hover .roll-letter-inner,
      .roll-letter.toggled .roll-letter-inner {{
        transform: none !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Skip link for keyboard accessibility -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- 1. FIXED TOP BAR -->
  <header class="header-bar" role="banner">
    <div class="container header-inner">
      <a href="#hero" class="brand-logo" aria-label="Karlsthetics Fitness Home">
        <!-- Ring-shaped weight-plate icon -->
        <svg class="ring-plate-icon" width="28" height="28" viewBox="0 0 32 32" fill="none" aria-hidden="true">
          <circle cx="16" cy="16" r="14" stroke="#F2B705" stroke-width="2.5" />
          <circle cx="16" cy="16" r="6" stroke="#C6F6A4" stroke-width="2" />
          <circle cx="16" cy="6" r="1.5" fill="#F2B705" />
          <circle cx="16" cy="26" r="1.5" fill="#F2B705" />
          <circle cx="6" cy="16" r="1.5" fill="#F2B705" />
          <circle cx="26" cy="16" r="1.5" fill="#F2B705" />
        </svg>
        <span class="brand-text">Karlsthetics Fitness</span>
      </a>

      <div class="header-actions">
        <!-- Theme toggle button -->
        <button id="themeToggleBtn" class="theme-toggle-btn" aria-label="Toggle light or dark theme" title="Toggle theme">
          <svg id="themeIconSun" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="display:none;">
            <circle cx="12" cy="12" r="5"></circle>
            <line x1="12" y1="1" x2="12" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="23"></line>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
            <line x1="1" y1="12" x2="3" y2="12"></line>
            <line x1="21" y1="12" x2="23" y2="12"></line>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
          </svg>
          <svg id="themeIconMoon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
          </svg>
        </button>

        <a href="#apply" class="btn btn-primary header-apply">Apply for coaching</a>
        <button id="menuOpenBtn" class="menu-trigger-btn" aria-expanded="false" aria-controls="fullMenuOverlay">
          <span>Menu</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
          </svg>
        </button>
      </div>
    </div>
  </header>

  <!-- 2. FULL-SCREEN MENU OVERLAY (mustard background, ink text) -->
  <div id="fullMenuOverlay" class="menu-overlay" role="dialog" aria-modal="true" aria-label="Main Navigation Menu">
    <div class="menu-overlay-header">
      <div style="display:flex; align-items:center; gap:0.6rem;">
        <svg class="ring-plate-icon" width="28" height="28" viewBox="0 0 32 32" fill="none" aria-hidden="true">
          <circle cx="16" cy="16" r="14" stroke="#101512" stroke-width="2.5" />
          <circle cx="16" cy="16" r="6" stroke="#101512" stroke-width="2" />
        </svg>
        <span style="font-family:var(--font-serif); font-weight:700; font-size:1.35rem; color:var(--ink);">Karlsthetics</span>
      </div>
      <button id="menuCloseBtn" class="menu-overlay-close" aria-label="Close menu">
        <span>Close</span>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
      </button>
    </div>

    <nav class="menu-nav-links" aria-label="Full screen links">
      <a href="#hero" class="menu-link-item">Home</a>
      <a href="#coaching" class="menu-link-item">Online coaching</a>
      <a href="#highlights" class="menu-link-item">Client highlights</a>
      <a href="#credentials" class="menu-link-item">Credentials</a>
      <a href="#apply" class="menu-link-item">Apply</a>
    </nav>

    <div class="menu-overlay-footer">
      <div>
        <p class="menu-footer-text">Science-based online coaching for training, nutrition and body composition.</p>
        <div class="menu-social-links" style="margin-top:0.6rem;">
          <a href="https://www.instagram.com/_karl01001011/" target="_blank" rel="noopener noreferrer" style="color:var(--ink); font-weight:700; text-decoration:underline;">Instagram</a>
          <span style="color:var(--ink); opacity:0.5;">&bull;</span>
          <a href="https://www.facebook.com/profile.php?id=61588582303501" target="_blank" rel="noopener noreferrer" style="color:var(--ink); font-weight:700; text-decoration:underline;">Facebook</a>
        </div>
      </div>
      <a href="#apply" class="btn btn-outline-dark" id="menuApplyCta">Apply for coaching</a>
    </div>
  </div>

  <main id="main-content">
    <!-- 3. HERO (dark turf, no photo) -->
    <section id="hero" class="hero-section" aria-labelledby="heroHeadline">
      <div class="container hero-container">
        <h1 id="heroHeadline" class="hero-headline">
          <span class="hero-line-mask"><span class="hero-line hero-line-1">Online fitness</span></span>
          <span class="hero-line-mask"><span class="hero-line hero-line-2">coaching built</span></span>
          <span class="hero-line-mask"><span class="hero-line hero-line-3">on evidence.</span></span>
        </h1>
        <p class="hero-copy">
          Training, nutrition and injury-aware programming, delivered to your phone and adjusted every week. Coached by a certified personal trainer and physique competitor with a background in physical therapy and nutrition.
        </p>
        <div class="hero-ctas">
          <a href="#apply" class="btn btn-primary">Apply for coaching</a>
          <a href="#highlights" class="btn btn-secondary">See client results</a>
        </div>

        <div class="hero-trust-bar">
          <div class="trust-badge">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>Science-Based Programming</span>
          </div>
          <div class="trust-badge">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>Injury &amp; PT Movement Screen</span>
          </div>
          <div class="trust-badge">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            <span>Weekly Video Form Check-Ins</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. TICKER (mustard band, infinite marquee, pauses on hover) -->
    <div class="ticker-band" aria-hidden="true">
      <div class="ticker-track">
        <div class="ticker-item">
          <span>Online coaching</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
        <div class="ticker-item">
          <span>Science-based</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
        <div class="ticker-item">
          <span>Certified personal trainer</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
        <div class="ticker-item">
          <span>Physique and classic competitor</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
        <div class="ticker-item">
          <span>Injury-aware training</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
        <div class="ticker-item">
          <span>Nutrition coaching</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
      </div>

      <!-- Cloned track for seamless infinite scroll -->
      <div class="ticker-track" aria-hidden="true">
        <div class="ticker-item">
          <span>Online coaching</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
        <div class="ticker-item">
          <span>Science-based</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
        <div class="ticker-item">
          <span>Certified personal trainer</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
        <div class="ticker-item">
          <span>Physique and classic competitor</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
        <div class="ticker-item">
          <span>Injury-aware training</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
        <div class="ticker-item">
          <span>Nutrition coaching</span>
          <svg class="ring-plate-icon" width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="#101512" stroke-width="2"/><circle cx="12" cy="12" r="4" stroke="#101512" stroke-width="1.8"/></svg>
        </div>
      </div>
    </div>

    <!-- 5. ONLINE COACHING (chalk background - main section) -->
    <section id="coaching" class="coaching-section section-pad" aria-labelledby="coachingMainHeading">
      <div class="container">
        <!-- Big statement sentence with inline graphic -->
        <div class="statement-banner">
          <p class="statement-sentence" id="coachingMainHeading">
            A real coach in your pocket 
            <span class="statement-pill" aria-label="phone icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <rect x="5" y="2" width="14" height="20" rx="3" ry="3"></rect>
                <line x1="12" y1="18" x2="12.01" y2="18"></line>
              </svg>
            </span> 
            not a PDF you never open.
          </p>
        </div>

        <div class="lede-grid">
          <p class="lede-p">
            <strong>Online coaching puts your program, nutrition targets and feedback in one place,</strong> and changes them as you change. No recycled spreadsheets or generic routines that stop working after two weeks.
          </p>
          <p class="lede-p">
            <strong>You train wherever you train.</strong> I review your check-ins, your training logs and your form videos, then adjust the plan based on what the numbers say, not what a template says.
          </p>
        </div>

        <!-- "How it works" Accessible Tabs Widget -->
        <div class="tabs-wrapper">
          <div class="tabs-heading-row">
            <h2 class="tabs-heading grad-chalk">How it works</h2>
            <span style="font-size:0.95rem; font-weight:600; color:var(--chalk-muted);">5-Step System</span>
          </div>

          <div class="tabs-layout">
            <!-- Left numbered vertical tab list -->
            <div class="tab-list" role="tablist" aria-label="Coaching process steps">
              <button class="tab-btn" role="tab" id="tab-1" aria-selected="true" aria-controls="panel-1" tabindex="0">
                <span class="tab-num">1</span>
                <span>Intake &amp; assessment</span>
              </button>
              <button class="tab-btn" role="tab" id="tab-2" aria-selected="false" aria-controls="panel-2" tabindex="-1">
                <span class="tab-num">2</span>
                <span>Program &amp; targets</span>
              </button>
              <button class="tab-btn" role="tab" id="tab-3" aria-selected="false" aria-controls="panel-3" tabindex="-1">
                <span class="tab-num">3</span>
                <span>Weekly check-ins</span>
              </button>
              <button class="tab-btn" role="tab" id="tab-4" aria-selected="false" aria-controls="panel-4" tabindex="-1">
                <span class="tab-num">4</span>
                <span>Adjustments</span>
              </button>
              <button class="tab-btn" role="tab" id="tab-5" aria-selected="false" aria-controls="panel-5" tabindex="-1">
                <span class="tab-num">5</span>
                <span>Form checks &amp; questions</span>
              </button>
            </div>

            <!-- Right content panels -->
            <div class="tab-panel-container">
              <!-- Panel 1 -->
              <div class="tab-panel active" id="panel-1" role="tabpanel" aria-labelledby="tab-1" tabindex="0">
                <h3 class="tab-panel-title">Intake and assessment</h3>
                <p class="tab-panel-desc">
                  We look at your specific goals, training history, injuries and weekly schedule. Short movement videos are screened using my physical therapy background to catch joint restrictions and technique bottlenecks before heavy lifting starts.
                </p>
                <div class="exchange-grid">
                  <div class="exchange-col">
                    <div class="exchange-col-title">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                      <span>You send</span>
                    </div>
                    <ul class="exchange-list">
                      <li>Goals and weekly training schedule</li>
                      <li>Injury history and pain points</li>
                      <li>Movement screening videos</li>
                    </ul>
                  </div>
                  <div class="exchange-col">
                    <div class="exchange-col-title">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                      <span>You get</span>
                    </div>
                    <ul class="exchange-list">
                      <li>A written starting assessment</li>
                      <li>Clear first-phase progression plan</li>
                      <li>Targeted mobility and warmup drills</li>
                    </ul>
                  </div>
                </div>
              </div>

              <!-- Panel 2 -->
              <div class="tab-panel" id="panel-2" role="tabpanel" aria-labelledby="tab-2" tabindex="0">
                <h3 class="tab-panel-title">Your program and targets</h3>
                <p class="tab-panel-desc">
                  A comprehensive plan built strictly around your actual schedule, available gym or home equipment, and recovery capacity. Plus calculated calorie and protein targets tailored for your body composition objective.
                </p>
                <div class="exchange-grid">
                  <div class="exchange-col">
                    <div class="exchange-col-title">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                      <span>You send</span>
                    </div>
                    <ul class="exchange-list">
                      <li>Gym or home equipment access</li>
                      <li>Food preferences and dietary habits</li>
                      <li>Grocery budget and meal routine</li>
                    </ul>
                  </div>
                  <div class="exchange-col">
                    <div class="exchange-col-title">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                      <span>You get</span>
                    </div>
                    <ul class="exchange-list">
                      <li>Customized progressive training program</li>
                      <li>Calorie and protein macro targets</li>
                      <li>Practical meal structure options</li>
                    </ul>
                  </div>
                </div>
              </div>

              <!-- Panel 3 -->
              <div class="tab-panel" id="panel-3" role="tabpanel" aria-labelledby="tab-3" tabindex="0">
                <h3 class="tab-panel-title">Weekly check-ins</h3>
                <p class="tab-panel-desc">
                  Every week you submit your 7-day average bodyweight, workout logs, sleep and energy metrics. Progress photos are always optional. We analyze actual trend lines rather than day-to-day noise.
                </p>
                <div class="exchange-grid">
                  <div class="exchange-col">
                    <div class="exchange-col-title">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                      <span>You send</span>
                    </div>
                    <ul class="exchange-list">
                      <li>Average bodyweight log</li>
                      <li>Notes on how lifting sessions felt</li>
                      <li>Sleep, stress and biofeedback markers (photos optional)</li>
                    </ul>
                  </div>
                  <div class="exchange-col">
                    <div class="exchange-col-title">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                      <span>You get</span>
                    </div>
                    <ul class="exchange-list">
                      <li>Written individual feedback on your week</li>
                      <li>Clear actionable next steps for the upcoming cycle</li>
                      <li>Direct accountability from your coach</li>
                    </ul>
                  </div>
                </div>
              </div>

              <!-- Panel 4 -->
              <div class="tab-panel" id="panel-4" role="tabpanel" aria-labelledby="tab-4" tabindex="0">
                <h3 class="tab-panel-title">Adjustments</h3>
                <p class="tab-panel-desc">
                  We change only one or two variables at a time—such as volume sets, load progression, calorie intake, or cardio frequency. This scientific isolation makes it completely obvious what drives your results.
                </p>
                <div class="exchange-grid">
                  <div class="exchange-col">
                    <div class="exchange-col-title">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                      <span>You send</span>
                    </div>
                    <ul class="exchange-list">
                      <li>Weekly data trends and strength logs</li>
                      <li>Biofeedback on hunger and fatigue</li>
                      <li>Schedule changes or travel plans</li>
                    </ul>
                  </div>
                  <div class="exchange-col">
                    <div class="exchange-col-title">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                      <span>You get</span>
                    </div>
                    <ul class="exchange-list">
                      <li>Targeted volume or macro calibrations</li>
                      <li>Deload or intensification protocols</li>
                      <li>Clear explanation of the rationale</li>
                    </ul>
                  </div>
                </div>
              </div>

              <!-- Panel 5 -->
              <div class="tab-panel" id="panel-5" role="tabpanel" aria-labelledby="tab-5" tabindex="0">
                <h3 class="tab-panel-title">Form checks and questions</h3>
                <p class="tab-panel-desc">
                  Whenever you're unsure about exercise execution, send over a video of your working set. You get direct biomechanical coaching notes, cue adjustments, and prompt answers between weekly check-ins.
                </p>
                <div class="exchange-grid">
                  <div class="exchange-col">
                    <div class="exchange-col-title">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
                      <span>You send</span>
                    </div>
                    <ul class="exchange-list">
                      <li>Working set exercise videos</li>
                      <li>Specific questions on technique or cues</li>
                      <li>Ad-hoc questions about dining out or fatigue</li>
                    </ul>
                  </div>
                  <div class="exchange-col">
                    <div class="exchange-col-title">
                      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                      <span>You get</span>
                    </div>
                    <ul class="exchange-list">
                      <li>Direct technique feedback and movement breakdown</li>
                      <li>Corrective execution cues</li>
                      <li>Timely support without waiting for check-in day</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Enticing Section: The Coaching Difference (Why 1-on-1 Outperforms Generic Templates) -->
        <div class="difference-card">
          <div class="diff-header">
            <span class="diff-badge">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
              <span>The Karlsthetics Edge</span>
            </span>
            <h3 class="diff-title grad-chalk">Why Generic Plans Fail &amp; Coaching Works</h3>
            <p class="diff-subtitle">Free online calculators and cookie-cutter routines treat everyone like an identical robot. 1-on-1 evidence-based coaching builds your strategy around your actual biology, schedule, and biomechanics.</p>
          </div>

          <div class="diff-matrix-grid">
            <!-- Generic Column -->
            <div class="diff-col diff-col-generic">
              <div class="diff-col-title-wrap">
                <span class="diff-col-title">Generic Apps &amp; Static Plans</span>
                <span class="diff-col-tag tag-stale">Cookie-Cutter</span>
              </div>
              <ul class="diff-list">
                <li class="diff-item">
                  <span class="diff-icon diff-icon-cross">&times;</span>
                  <div class="diff-text">
                    <span class="diff-text-headline">One-Size-Fits-All Numbers</span>
                    <span class="diff-text-desc">Generic calculators give arbitrary calorie and macro numbers that completely ignore metabolic slowdown, daily step counts, and lifestyle realities.</span>
                  </div>
                </li>
                <li class="diff-item">
                  <span class="diff-icon diff-icon-cross">&times;</span>
                  <div class="diff-text">
                    <span class="diff-text-headline">Ignored Joint Pain &amp; Injuries</span>
                    <span class="diff-text-desc">Templates force you into standard lifts. If your knees, lower back, or shoulders hurt, you are left to guess or forced to stop training.</span>
                  </div>
                </li>
                <li class="diff-item">
                  <span class="diff-icon diff-icon-cross">&times;</span>
                  <div class="diff-text">
                    <span class="diff-text-headline">Zero Form Video Feedback</span>
                    <span class="diff-text-desc">You never know if your technique, depth, and bar path are optimal, risking injury and missing true mechanical tension.</span>
                  </div>
                </li>
                <li class="diff-item">
                  <span class="diff-icon diff-icon-cross">&times;</span>
                  <div class="diff-text">
                    <span class="diff-text-headline">No Adjustments When Stalled</span>
                    <span class="diff-text-desc">When progress inevitably plateaus after 3 weeks, you are left stranded with no protocol to break through.</span>
                  </div>
                </li>
              </ul>
            </div>

            <!-- Karlsthetics Column -->
            <div class="diff-col diff-col-coach">
              <div class="diff-col-title-wrap">
                <span class="diff-col-title">Karlsthetics 1-on-1 Coaching</span>
                <span class="diff-col-tag tag-premium">Evidence-Based</span>
              </div>
              <ul class="diff-list">
                <li class="diff-item">
                  <span class="diff-icon diff-icon-check">&#10003;</span>
                  <div class="diff-text">
                    <span class="diff-text-headline">Custom Nutrition Protocol &amp; Weekly Shifts</span>
                    <span class="diff-text-desc">Targets calculated specifically for your body composition, then adjusted weekly based on your scale trend lines and biofeedback.</span>
                  </div>
                </li>
                <li class="diff-item">
                  <span class="diff-icon diff-icon-check">&#10003;</span>
                  <div class="diff-text">
                    <span class="diff-text-headline">Physical Therapy Screened Programming</span>
                    <span class="diff-text-desc">Joint angles, grip widths, and resistance curves customized around your pain history so you train hard without breaking down.</span>
                  </div>
                </li>
                <li class="diff-item">
                  <span class="diff-icon diff-icon-check">&#10003;</span>
                  <div class="diff-text">
                    <span class="diff-text-headline">Direct Frame-by-Frame Form Checks</span>
                    <span class="diff-text-desc">Send working set videos and receive expert feedback and technical cues to maximize muscle recruitment safely.</span>
                  </div>
                </li>
                <li class="diff-item">
                  <span class="diff-icon diff-icon-check">&#10003;</span>
                  <div class="diff-text">
                    <span class="diff-text-headline">Weekly Sunday Accountability &amp; Calibrations</span>
                    <span class="diff-text-desc">Comprehensive audits of workout volume, fatigue, and recovery markers to ensure you never stay stuck in a plateau.</span>
                  </div>
                </li>
              </ul>
            </div>
          </div>

          <div class="diff-footer-cta">
            <p class="diff-footer-msg">Stop guessing your numbers and wasting months on routines that stall. Get a tailored plan calibrated every single week.</p>
            <a href="#apply" class="btn btn-primary" style="box-shadow: 0 4px 14px rgba(242, 183, 5, 0.35);">
              <span>Apply for 1-on-1 Coaching</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
          </div>
        </div>

        <!-- "A sample week" widget -->
        <div class="sample-week-wrapper">
          <div class="sample-week-header">
            <h3 class="sample-week-title grad-chalk">A sample week</h3>
            <p class="sample-week-caption">Your schedule and equipment set the real one.</p>
          </div>

          <div class="day-buttons-scroll" role="group" aria-label="Sample training week days">
            <button class="day-btn" data-day="mon" aria-pressed="true">
              <span class="day-name">Mon</span>
              <span class="day-focus">Upper body</span>
            </button>
            <button class="day-btn" data-day="tue" aria-pressed="false">
              <span class="day-name">Tue</span>
              <span class="day-focus">Lower body</span>
            </button>
            <button class="day-btn" data-day="wed" aria-pressed="false">
              <span class="day-name">Wed</span>
              <span class="day-focus">Recovery</span>
            </button>
            <button class="day-btn" data-day="thu" aria-pressed="false">
              <span class="day-name">Thu</span>
              <span class="day-focus">Upper body</span>
            </button>
            <button class="day-btn" data-day="fri" aria-pressed="false">
              <span class="day-name">Fri</span>
              <span class="day-focus">Lower body</span>
            </button>
            <button class="day-btn" data-day="sat" aria-pressed="false">
              <span class="day-name">Sat</span>
              <span class="day-focus">Your choice</span>
            </button>
            <button class="day-btn" data-day="sun" aria-pressed="false">
              <span class="day-name">Sun</span>
              <span class="day-focus">Check-in</span>
            </button>
          </div>

          <!-- One-sentence description updated live -->
          <div class="day-detail-box" aria-live="polite">
            <svg class="ring-plate-icon" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F2B705" stroke-width="2.2" aria-hidden="true">
              <circle cx="12" cy="12" r="10"></circle>
              <polyline points="12 6 12 12 16 14"></polyline>
            </svg>
            <span id="dayDetailText" class="day-detail-text">
              Monday: Heavy compound pressing and pulling with calibrated accessory volume to build the upper frame.
            </span>
          </div>
        </div>
      </div>
    </section>

    <!-- 6. CLIENT HIGHLIGHTS (dark turf) -->
    <section id="highlights" class="highlights-section section-pad" aria-labelledby="highlightsHeading">
      <div class="container">
        <div class="highlights-header">
          <h2 id="highlightsHeading" class="highlights-title grad-turf">Client highlights</h2>
          <p class="highlights-subtext">
            Real client results. Drag, scroll or use the arrows, and tap a photo to enlarge it.
          </p>
        </div>

        <!-- Filter Chips & Carousel Counter / Controls -->
        <div class="highlights-controls-row">
          <div class="chip-group" role="group" aria-label="Filter results by category">
            <button class="chip active" data-filter="all" aria-pressed="true">All</button>
            <button class="chip" data-filter="fat-loss" aria-pressed="false">Fat loss</button>
            <button class="chip" data-filter="muscle-gain" aria-pressed="false">Muscle gain</button>
            <button class="chip" data-filter="recomp" aria-pressed="false">Recomposition</button>
          </div>

          <div class="carousel-nav-controls">
            <span id="carouselCounter" class="carousel-counter" aria-live="polite">1 / 3</span>
            <button id="carouselPrevBtn" class="carousel-round-btn" aria-label="Previous client slide">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <polyline points="15 18 9 12 15 6"></polyline>
              </svg>
            </button>
            <button id="carouselNextBtn" class="carousel-round-btn" aria-label="Next client slide">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <polyline points="9 18 15 12 9 6"></polyline>
              </svg>
            </button>
          </div>
        </div>
      </div>

      <!-- Horizontal draggable scroll-snap carousel -->
      <div id="carouselViewport" class="carousel-viewport" tabindex="0" role="region" aria-label="Client results carousel">
        <div class="carousel-track" id="carouselTrack">
          <!-- Card 1: Fat loss -->
          <article class="highlight-card" data-category="fat-loss">
            <div class="card-photo-wrapper" role="button" tabindex="0" aria-label="Enlarge Fat loss transformation photo" data-full-src="{img_fatloss}" data-full-caption="Fat loss: From 105 kg to 79.5 kg (−25.5 kg), with far more visible muscle definition at the end. Faces hidden for privacy.">
              <span class="gold-tag-pill">−25.5 kg</span>
              <img class="card-photo" src="{img_fatloss}" alt="Client before and after fat loss from 105kg to 79.5kg, faces are hidden to protect client privacy" loading="lazy">
              <span class="card-zoom-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
                <span>Tap to enlarge</span>
              </span>
            </div>
            <div class="card-content">
              <span class="card-category">Fat loss</span>
              <p class="card-caption">From 105 kg to 79.5 kg, with far more visible muscle definition at the end.</p>
            </div>
          </article>

          <!-- Card 2: Muscle gain -->
          <article class="highlight-card" data-category="muscle-gain">
            <div class="card-photo-wrapper" role="button" tabindex="0" aria-label="Enlarge Muscle gain transformation photo" data-full-src="{img_muscle}" data-full-caption="Muscle gain: Bodyweight up from 50 kg to 67 kg (+17 kg), with a much fuller, more muscular frame. Faces hidden for privacy.">
              <span class="gold-tag-pill">+17 kg</span>
              <img class="card-photo" src="{img_muscle}" alt="Client before and after muscle gain from 50kg to 67kg, faces are hidden to protect client privacy" loading="lazy">
              <span class="card-zoom-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
                <span>Tap to enlarge</span>
              </span>
            </div>
            <div class="card-content">
              <span class="card-category">Muscle gain</span>
              <p class="card-caption">Bodyweight up from 50 kg to 67 kg, with a much fuller, more muscular frame.</p>
            </div>
          </article>

          <!-- Card 3: Recomposition -->
          <article class="highlight-card" data-category="recomp">
            <div class="card-photo-wrapper" role="button" tabindex="0" aria-label="Enlarge Recomposition transformation photo" data-full-src="{img_recomp}" data-full-caption="Recomposition: Leaner, fuller. Less fat around the midsection and more visible muscle through the shoulders and arms. Faces hidden for privacy.">
              <span class="gold-tag-pill">Leaner, fuller</span>
              <img class="card-photo" src="{img_recomp}" alt="Client before and after body recomposition, faces are hidden to protect client privacy" loading="lazy">
              <span class="card-zoom-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line><line x1="11" y1="8" x2="11" y2="14"></line><line x1="8" y1="11" x2="14" y2="11"></line></svg>
                <span>Tap to enlarge</span>
              </span>
            </div>
            <div class="card-content">
              <span class="card-category">Body recomposition</span>
              <p class="card-caption">Less fat around the midsection and more visible muscle through the shoulders and arms.</p>
            </div>
          </article>
        </div>
      </div>

      <div class="container">
        <p class="highlights-fine-print">
          Faces are hidden to protect client privacy. Results depend on starting point, consistency and lifestyle, and no result is guaranteed.
        </p>
      </div>
    </section>

    <!-- Lightbox Dialog for Full Photo View -->
    <dialog id="photoLightbox" class="lightbox-dialog" aria-labelledby="lightboxCaption">
      <div class="lightbox-inner">
        <div class="lightbox-header">
          <span class="lightbox-title">Client Highlight</span>
          <button id="lightboxCloseBtn" class="lightbox-close" aria-label="Close dialog">Close &times;</button>
        </div>
        <div class="lightbox-img-wrapper">
          <img id="lightboxImg" class="lightbox-img" src="" alt="Client transformation enlarged view">
        </div>
        <div id="lightboxCaption" class="lightbox-caption"></div>
      </div>
    </dialog>

    <!-- 7. CREDENTIALS (chalk) -->
    <section id="credentials" class="credentials-section section-pad" aria-labelledby="credentialsHeading">
      <div class="container">
        <div class="credentials-header">
          <h2 id="credentialsHeading" class="credentials-title grad-chalk">Credentials</h2>
          <p class="credentials-lede">
            Each one changes how your coaching works. Pick a topic to see which ones apply.
          </p>
        </div>

        <!-- Filter Chips: All, Training, Nutrition, Injuries, Physique -->
        <div class="chip-group credentials-chips" role="group" aria-label="Filter credentials by topic">
          <button class="chip active" data-cred-filter="all" aria-pressed="true">All</button>
          <button class="chip" data-cred-filter="training" aria-pressed="false">Training</button>
          <button class="chip" data-cred-filter="nutrition" aria-pressed="false">Nutrition</button>
          <button class="chip" data-cred-filter="injuries" aria-pressed="false">Injuries</button>
          <button class="chip" data-cred-filter="physique" aria-pressed="false">Physique</button>
        </div>

        <!-- Accordion List with Big Serif Rows (Row 1 open by default) -->
        <div class="accordion-list" role="region" aria-label="Coach credentials accordion">
          
          <!-- Item 1: Certified personal trainer -->
          <div class="accordion-item" data-topics="training">
            <button class="accordion-btn" id="acc-btn-1" aria-expanded="true" aria-controls="acc-panel-1">
              <div class="accordion-title-wrap">
                <span>Certified personal trainer</span>
                <span class="accordion-tags"><span class="acc-tag">Training</span></span>
              </div>
              <span class="accordion-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
              </span>
            </button>
            <div class="accordion-collapse open" id="acc-panel-1" role="region" aria-labelledby="acc-btn-1">
              <div class="accordion-body">
                <div class="accordion-content">
                  Comprehensive program design, biomechanical lifting technique, and safe progressive overload protocols. Every routine is built specifically around your current training age, weekly schedule, and available gym or home equipment.
                </div>
              </div>
            </div>
          </div>

          <!-- Item 2: Physique and classic competitor -->
          <div class="accordion-item" data-topics="physique training nutrition">
            <button class="accordion-btn" id="acc-btn-2" aria-expanded="false" aria-controls="acc-panel-2">
              <div class="accordion-title-wrap">
                <span>Physique and classic competitor</span>
                <span class="accordion-tags"><span class="acc-tag">Physique</span><span class="acc-tag">Training</span><span class="acc-tag">Nutrition</span></span>
              </div>
              <span class="accordion-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
              </span>
            </button>
            <div class="accordion-collapse" id="acc-panel-2" role="region" aria-labelledby="acc-btn-2">
              <div class="accordion-body">
                <div class="accordion-content">
                  Knows from the inside what it takes to build muscle, diet down and hold a physique; can coach show prep. Having stepped on stage personally, I understand the psychological and physiological demands of pushing body composition to the edge.
                </div>
              </div>
            </div>
          </div>

          <!-- Item 3: Physical therapy background -->
          <div class="accordion-item" data-topics="injuries">
            <button class="accordion-btn" id="acc-btn-3" aria-expanded="false" aria-controls="acc-panel-3">
              <div class="accordion-title-wrap">
                <span>Physical therapy background</span>
                <span class="accordion-tags"><span class="acc-tag">Injuries</span></span>
              </div>
              <span class="accordion-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
              </span>
            </button>
            <div class="accordion-collapse" id="acc-panel-3" role="region" aria-labelledby="acc-btn-3">
              <div class="accordion-body">
                <div class="accordion-content">
                  Screens movement before programming and works around pain and past injuries. We adapt joint angles, grip widths, and loading curves so you train hard without breaking down. This is coaching, not medical treatment or diagnosis. If you have a medical condition, we work alongside your doctor.
                </div>
              </div>
            </div>
          </div>

          <!-- Item 4: Nutrition background -->
          <div class="accordion-item" data-topics="nutrition">
            <button class="accordion-btn" id="acc-btn-4" aria-expanded="false" aria-controls="acc-panel-4">
              <div class="accordion-title-wrap">
                <span>Nutrition background</span>
                <span class="accordion-tags"><span class="acc-tag">Nutrition</span></span>
              </div>
              <span class="accordion-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
              </span>
            </button>
            <div class="accordion-collapse" id="acc-panel-4" role="region" aria-labelledby="acc-btn-4">
              <div class="accordion-body">
                <div class="accordion-content">
                  Evidence-based calorie and protein targets, customized meal timing strategies, and systematic adjustments based strictly on weight trend lines. Flexible and structured for real life, social meals, and sustainable adherence.
                </div>
              </div>
            </div>
          </div>

          <!-- Item 5: Science-based approach -->
          <div class="accordion-item" data-topics="training nutrition">
            <button class="accordion-btn" id="acc-btn-5" aria-expanded="false" aria-controls="acc-panel-5">
              <div class="accordion-title-wrap">
                <span>Science-based approach</span>
                <span class="accordion-tags"><span class="acc-tag">Training</span><span class="acc-tag">Nutrition</span></span>
              </div>
              <span class="accordion-icon" aria-hidden="true">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
              </span>
            </button>
            <div class="accordion-collapse" id="acc-panel-5" role="region" aria-labelledby="acc-btn-5">
              <div class="accordion-body">
                <div class="accordion-content">
                  Follows research on effective volume landmarks, progressive overload metrics, dietary protein distribution and recovery management. We test what works, track data objectively, and change course whenever evidence points the way.
                </div>
              </div>
            </div>
          </div>

        </div>

        <div class="credentials-disclaimer">
          Coaching offers fitness and nutrition guidance and is not medical advice. Check with your doctor before starting a new program if you have a health condition.
        </div>
      </div>
    </section>

    <!-- 8. APPLY (full mustard block) -->
    <section id="apply" class="apply-section section-pad" aria-labelledby="applyHeading">
      <div class="container">
        <div class="apply-header">
          <h2 id="applyHeading" class="apply-title">Tell me where you're starting.</h2>
          <p class="apply-lede">
            Answer four quick questions and I'll write your application message for you. Copy it and send it directly to me on Instagram or Facebook.
          </p>
        </div>

        <div class="apply-grid">
          <!-- Form-Free Builder Controls -->
          <div class="builder-card">
            <!-- 1. Name input -->
            <div class="builder-field">
              <label for="applyName" class="builder-label">Your Name</label>
              <input type="text" id="applyName" class="builder-input" placeholder="e.g. Alex" autocomplete="name">
            </div>

            <!-- 2. Main goal -->
            <div class="builder-field">
              <span class="builder-label">Main goal</span>
              <div class="builder-chips" role="group" aria-label="Main goal selection" data-builder-group="goal">
                <button type="button" class="b-chip" data-val="Lose fat" aria-pressed="false">Lose fat</button>
                <button type="button" class="b-chip" data-val="Build muscle" aria-pressed="false">Build muscle</button>
                <button type="button" class="b-chip" data-val="Recomposition" aria-pressed="false">Recomposition</button>
                <button type="button" class="b-chip" data-val="Prepare for a show" aria-pressed="false">Prepare for a show</button>
              </div>
            </div>

            <!-- 3. Training experience -->
            <div class="builder-field">
              <span class="builder-label">Training experience</span>
              <div class="builder-chips" role="group" aria-label="Training experience selection" data-builder-group="experience">
                <button type="button" class="b-chip" data-val="Beginner" aria-pressed="false">Beginner</button>
                <button type="button" class="b-chip" data-val="Some experience" aria-pressed="false">Some experience</button>
                <button type="button" class="b-chip" data-val="Advanced" aria-pressed="false">Advanced</button>
              </div>
            </div>

            <!-- 4. Injuries or pain -->
            <div class="builder-field">
              <span class="builder-label">Injuries or pain</span>
              <div class="builder-chips" role="group" aria-label="Injuries or pain selection" data-builder-group="injuries">
                <button type="button" class="b-chip" data-val="None" aria-pressed="false">None</button>
                <button type="button" class="b-chip" data-val="Past injury" aria-pressed="false">Past injury</button>
                <button type="button" class="b-chip" data-val="Current pain" aria-pressed="false">Current pain</button>
              </div>
            </div>

            <!-- 5. Where you train -->
            <div class="builder-field">
              <span class="builder-label">Where you train</span>
              <div class="builder-chips" role="group" aria-label="Where you train selection" data-builder-group="location">
                <button type="button" class="b-chip" data-val="Gym" aria-pressed="false">Gym</button>
                <button type="button" class="b-chip" data-val="Home" aria-pressed="false">Home</button>
                <button type="button" class="b-chip" data-val="Both" aria-pressed="false">Both</button>
              </div>
            </div>

            <!-- Optional: Anything else -->
            <div class="builder-field">
              <label for="applyNotes" class="builder-label">Anything else (optional)</label>
              <input type="text" id="applyNotes" class="builder-input" placeholder="e.g. Busy work schedule, knee soreness with heavy squats">
            </div>
          </div>

          <!-- Live Generated Message Preview & Copy Actions -->
          <div class="preview-card">
            <div class="preview-header">
              <span class="preview-title">Your Generated Application</span>
              <span style="font-size:0.85rem; font-weight:700; color:var(--moss);">Live Preview</span>
            </div>

            <textarea id="applyMessageOutput" class="preview-textarea" readonly aria-label="Generated coaching application message"></textarea>

            <div class="preview-actions">
              <button id="copyMessageBtn" class="btn btn-copy" type="button">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                  <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                  <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                <span>Copy message</span>
              </button>
              <div id="copyStatusLine" class="copy-status" aria-live="polite"></div>
            </div>

            <!-- Prominent Social Media Direct Send Section inside White Box -->
            <div class="contact-channels" id="contactChannelsBlock">
              <span class="contact-channels-label">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
                <span>Send message directly to Coach Karl:</span>
              </span>
              <div class="social-buttons-grid">
                <a href="https://www.instagram.com/_karl01001011/" target="_blank" rel="noopener noreferrer" class="social-action-btn instagram-btn" id="sendInstagramBtn">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
                  </svg>
                  <span>Instagram DM</span>
                </a>
                <a href="https://www.facebook.com/profile.php?id=61588582303501" target="_blank" rel="noopener noreferrer" class="social-action-btn facebook-btn" id="sendFacebookBtn">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                    <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                  </svg>
                  <span>Facebook Messenger</span>
                </a>
              </div>
              <p class="social-sub-note">💡 Clicking either button automatically copies your text above so you can simply paste it directly into Karl's chat.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Floating Apply Action Pill -->
  <a href="#apply" class="floating-action-pill" id="floatingApplyBtn" aria-label="Quick apply for coaching">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
    <span>Apply for Coaching</span>
  </a>

  <!-- 9. FOOTER (turf) -->
  <footer class="footer-section" role="contentinfo">
    <div class="container">
      <div class="footer-cta-row">
        <h2 class="footer-headline font-serif grad-turf">Ready to train with a plan?</h2>
        <nav aria-label="Footer links">
          <ul class="footer-nav-list">
            <li><a href="#hero">Home</a></li>
            <li><a href="#coaching">Online coaching</a></li>
            <li><a href="#highlights">Client highlights</a></li>
            <li><a href="#credentials">Credentials</a></li>
            <li>
              <a href="https://www.instagram.com/_karl01001011/" target="_blank" rel="noopener noreferrer" class="footer-social-pill">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                <span>Instagram</span>
              </a>
            </li>
            <li>
              <a href="https://www.facebook.com/profile.php?id=61588582303501" target="_blank" rel="noopener noreferrer" class="footer-social-pill">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                <span>Facebook</span>
              </a>
            </li>
            <li><a href="#apply" class="btn btn-primary" style="padding:0.6rem 1.4rem; font-size:0.92rem;">Apply for coaching</a></li>
          </ul>
        </nav>
      </div>

      <!-- Giant two-row wordmark: Karlsthetics left-aligned, Fitness right-aligned -->
      <div class="wordmark-container" id="wordmarkWrap" aria-label="Karlsthetics Fitness Wordmark">
        <div class="wordmark-row wordmark-row-1" id="wordmarkRow1">
          <!-- Populated by JS for clipped roll letters -->
        </div>
        <div class="wordmark-row wordmark-row-2" id="wordmarkRow2">
          <!-- Populated by JS for clipped roll letters -->
        </div>
      </div>

      <div class="footer-legal-bar">
        <p>Coaching offers fitness and nutrition guidance and is not medical advice. Results vary from person to person.</p>
        <p>&copy; <span id="currentYear"></span> Karlsthetics Fitness. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <!-- SCRIPT: Interactions, Tabs, Carousel, Builder, Wordmark -->
  <script>
    /* Coach Contact Configuration */
    const CONTACT = {{
      instagram: "https://www.instagram.com/_karl01001011/",
      facebook: "https://www.facebook.com/profile.php?id=61588582303501",
      email: ""
    }};

    document.addEventListener("DOMContentLoaded", () => {{
      // Update copyright year
      const yearEl = document.getElementById("currentYear");
      if (yearEl) yearEl.textContent = new Date().getFullYear();

      /* -----------------------------------------------------------
         1. THEME TOGGLING (In-memory dataset)
         ----------------------------------------------------------- */
      const themeToggleBtn = document.getElementById("themeToggleBtn");
      const themeIconSun = document.getElementById("themeIconSun");
      const themeIconMoon = document.getElementById("themeIconMoon");

      function updateThemeIcons(theme) {{
        if (theme === "dark") {{
          themeIconSun.style.display = "block";
          themeIconMoon.style.display = "none";
        }} else {{
          themeIconSun.style.display = "none";
          themeIconMoon.style.display = "block";
        }}
      }}

      const prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
      let currentTheme = prefersDark ? "dark" : "light";
      updateThemeIcons(currentTheme);

      if (themeToggleBtn) {{
        themeToggleBtn.addEventListener("click", () => {{
          currentTheme = currentTheme === "dark" ? "light" : "dark";
          document.documentElement.dataset.theme = currentTheme;
          updateThemeIcons(currentTheme);
        }});
      }}

      /* -----------------------------------------------------------
         2. FULL-SCREEN MENU OVERLAY (Trap Focus, Dim on Hover, Esc)
         ----------------------------------------------------------- */
      const menuOverlay = document.getElementById("fullMenuOverlay");
      const menuOpenBtn = document.getElementById("menuOpenBtn");
      const menuCloseBtn = document.getElementById("menuCloseBtn");
      const menuLinks = menuOverlay.querySelectorAll(".menu-link-item, #menuApplyCta");
      let previouslyFocusedElement = null;

      function openMenu() {{
        previouslyFocusedElement = document.activeElement;
        menuOverlay.classList.add("active");
        menuOpenBtn.setAttribute("aria-expanded", "true");
        document.body.style.overflow = "hidden";
        menuCloseBtn.focus();
      }}

      function closeMenu() {{
        menuOverlay.classList.remove("active");
        menuOpenBtn.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
        if (previouslyFocusedElement) previouslyFocusedElement.focus();
      }}

      if (menuOpenBtn) menuOpenBtn.addEventListener("click", openMenu);
      if (menuCloseBtn) menuCloseBtn.addEventListener("click", closeMenu);

      menuLinks.forEach(link => {{
        link.addEventListener("click", () => {{
          closeMenu();
        }});
      }});

      window.addEventListener("keydown", (e) => {{
        if (e.key === "Escape" && menuOverlay.classList.contains("active")) {{
          closeMenu();
        }}
        if (menuOverlay.classList.contains("active") && e.key === "Tab") {{
          const focusables = menuOverlay.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
          if (focusables.length === 0) return;
          const firstFocusable = focusables[0];
          const lastFocusable = focusables[focusables.length - 1];

          if (e.shiftKey) {{
            if (document.activeElement === firstFocusable) {{
              e.preventDefault();
              lastFocusable.focus();
            }}
          }} else {{
            if (document.activeElement === lastFocusable) {{
              e.preventDefault();
              firstFocusable.focus();
            }}
          }}
        }}
      }});

      /* -----------------------------------------------------------
         3. ACCESSIBLE TABS WIDGET (Online Coaching)
         ----------------------------------------------------------- */
      const tabButtons = Array.from(document.querySelectorAll('.tab-btn'));
      const tabPanels = Array.from(document.querySelectorAll('.tab-panel'));

      function activateTab(targetIndex) {{
        tabButtons.forEach((btn, idx) => {{
          const isSelected = idx === targetIndex;
          btn.setAttribute("aria-selected", isSelected ? "true" : "false");
          btn.setAttribute("tabindex", isSelected ? "0" : "-1");
        }});
        tabPanels.forEach((panel, idx) => {{
          if (idx === targetIndex) {{
            panel.classList.add("active");
          }} else {{
            panel.classList.remove("active");
          }}
        }});
      }}

      tabButtons.forEach((btn, index) => {{
        btn.addEventListener("click", () => {{
          activateTab(index);
        }});

        btn.addEventListener("keydown", (e) => {{
          let newIndex = null;
          if (e.key === "ArrowDown" || e.key === "ArrowRight") {{
            e.preventDefault();
            newIndex = (index + 1) % tabButtons.length;
          }} else if (e.key === "ArrowUp" || e.key === "ArrowLeft") {{
            e.preventDefault();
            newIndex = (index - 1 + tabButtons.length) % tabButtons.length;
          }} else if (e.key === "Home") {{
            e.preventDefault();
            newIndex = 0;
          }} else if (e.key === "End") {{
            e.preventDefault();
            newIndex = tabButtons.length - 1;
          }}

          if (newIndex !== null) {{
            tabButtons[newIndex].focus();
            activateTab(newIndex);
          }}
        }});
      }});

      /* -----------------------------------------------------------
         4. A SAMPLE WEEK INTERACTION
         ----------------------------------------------------------- */
      const dayData = {{
        mon: "Monday: Heavy compound pressing and pulling with calibrated accessory volume to build the upper frame.",
        tue: "Tuesday: Squat or leg press progression, hinge work, and hamstring curls built around knee and hip health.",
        wed: "Wednesday: Active recovery, mobility routines, step target review and central nervous system replenishment.",
        thu: "Thursday: Targeted upper body volume focusing on shoulders, back width, chest isolation and arms.",
        fri: "Friday: Posterior chain loading, lunges or split squats, calves, and core bracing drills.",
        sat: "Saturday: Optional extra cardio, conditioning, outdoor sport, or full rest depending on recovery status.",
        sun: "Sunday: Check-in morning! Submit average scale weight, training logs, fatigue score, and receive adjustments."
      }};

      const dayButtons = document.querySelectorAll('.day-btn');
      const dayDetailText = document.getElementById('dayDetailText');

      dayButtons.forEach(btn => {{
        btn.addEventListener("click", () => {{
          dayButtons.forEach(b => b.setAttribute("aria-pressed", "false"));
          btn.setAttribute("aria-pressed", "true");
          const day = btn.dataset.day;
          if (dayData[day] && dayDetailText) {{
            dayDetailText.textContent = dayData[day];
          }}
        }});
      }});

      /* -----------------------------------------------------------
         5. CLIENT HIGHLIGHTS: CAROUSEL, FILTERING, DRAG & LIGHTBOX
         ----------------------------------------------------------- */
      const carouselViewport = document.getElementById("carouselViewport");
      const carouselCards = Array.from(document.querySelectorAll(".highlight-card"));
      const carouselCounter = document.getElementById("carouselCounter");
      const prevBtn = document.getElementById("carouselPrevBtn");
      const nextBtn = document.getElementById("carouselNextBtn");
      const highlightFilterChips = document.querySelectorAll('[data-filter]');

      let currentFilteredCards = [...carouselCards];

      function updateCarouselCounter() {{
        if (currentFilteredCards.length === 0) {{
          carouselCounter.textContent = "0 / 0";
          return;
        }}
        const scrollLeft = carouselViewport.scrollLeft;
        let activeIdx = 0;
        let minDiff = Infinity;

        currentFilteredCards.forEach((card, idx) => {{
          const diff = Math.abs(card.offsetLeft - carouselViewport.offsetLeft - scrollLeft);
          if (diff < minDiff) {{
            minDiff = diff;
            activeIdx = idx;
          }}
        }});

        carouselCounter.textContent = `${{activeIdx + 1}} / ${{currentFilteredCards.length}}`;
        prevBtn.disabled = activeIdx === 0;
        nextBtn.disabled = activeIdx >= currentFilteredCards.length - 1;
      }}

      highlightFilterChips.forEach(chip => {{
        chip.addEventListener("click", () => {{
          highlightFilterChips.forEach(c => {{
            c.classList.remove("active");
            c.setAttribute("aria-pressed", "false");
          }});
          chip.classList.add("active");
          chip.setAttribute("aria-pressed", "true");

          const filter = chip.dataset.filter;
          carouselCards.forEach(card => {{
            const cat = card.dataset.category;
            if (filter === "all" || cat === filter) {{
              card.classList.remove("hidden");
            }} else {{
              card.classList.add("hidden");
            }}
          }});

          currentFilteredCards = carouselCards.filter(c => !c.classList.contains("hidden"));
          carouselViewport.scrollLeft = 0;
          updateCarouselCounter();
        }});
      }});

      prevBtn.addEventListener("click", () => {{
        const scrollAmount = carouselCards[0].offsetWidth + 24;
        carouselViewport.scrollBy({{ left: -scrollAmount, behavior: "smooth" }});
      }});
      nextBtn.addEventListener("click", () => {{
        const scrollAmount = carouselCards[0].offsetWidth + 24;
        carouselViewport.scrollBy({{ left: scrollAmount, behavior: "smooth" }});
      }});

      carouselViewport.addEventListener("scroll", () => {{
        updateCarouselCounter();
      }}, {{ passive: true }});

      let isDown = false;
      let startX = 0;
      let scrollStart = 0;
      let dragged = false;

      carouselViewport.addEventListener("mousedown", (e) => {{
        isDown = true;
        dragged = false;
        carouselViewport.classList.add("is-dragging");
        startX = e.pageX - carouselViewport.offsetLeft;
        scrollStart = carouselViewport.scrollLeft;
      }});

      window.addEventListener("mouseup", () => {{
        if (!isDown) return;
        isDown = false;
        carouselViewport.classList.remove("is-dragging");
      }});

      carouselViewport.addEventListener("mousemove", (e) => {{
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - carouselViewport.offsetLeft;
        const walk = (x - startX) * 1.5;
        if (Math.abs(walk) > 4) dragged = true;
        carouselViewport.scrollLeft = scrollStart - walk;
      }});

      // Lightbox Dialog
      const lightbox = document.getElementById("photoLightbox");
      const lightboxImg = document.getElementById("lightboxImg");
      const lightboxCaption = document.getElementById("lightboxCaption");
      const lightboxCloseBtn = document.getElementById("lightboxCloseBtn");

      document.querySelectorAll(".card-photo-wrapper").forEach(wrapper => {{
        function triggerLightbox() {{
          if (dragged) return;
          const fullSrc = wrapper.dataset.fullSrc;
          const fullCaption = wrapper.dataset.fullCaption;
          lightboxImg.src = fullSrc;
          lightboxCaption.textContent = fullCaption;
          if (typeof lightbox.showModal === "function") {{
            lightbox.showModal();
          }} else {{
            lightbox.setAttribute("open", "true");
          }}
        }}

        wrapper.addEventListener("click", triggerLightbox);
        wrapper.addEventListener("keydown", (e) => {{
          if (e.key === "Enter" || e.key === " ") {{
            e.preventDefault();
            triggerLightbox();
          }}
        }});
      }});

      if (lightboxCloseBtn) {{
        lightboxCloseBtn.addEventListener("click", () => {{
          lightbox.close();
        }});
      }}
      lightbox.addEventListener("click", (e) => {{
        const rect = lightbox.getBoundingClientRect();
        const isInDialog = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height
          && rect.left <= e.clientX && e.clientX <= rect.left + rect.width);
        if (!isInDialog) {{
          lightbox.close();
        }}
      }});

      updateCarouselCounter();

      /* -----------------------------------------------------------
         6. CREDENTIALS ACCORDION & TOPIC FILTERING
         ----------------------------------------------------------- */
      const credFilterChips = document.querySelectorAll('[data-cred-filter]');
      const accordionItems = Array.from(document.querySelectorAll('.accordion-item'));

      accordionItems.forEach(item => {{
        const btn = item.querySelector('.accordion-btn');
        const collapse = item.querySelector('.accordion-collapse');

        btn.addEventListener("click", () => {{
          const isExpanded = btn.getAttribute("aria-expanded") === "true";
          btn.setAttribute("aria-expanded", isExpanded ? "false" : "true");
          if (isExpanded) {{
            collapse.classList.remove("open");
          }} else {{
            collapse.classList.add("open");
          }}
        }});
      }});

      credFilterChips.forEach(chip => {{
        chip.addEventListener("click", () => {{
          credFilterChips.forEach(c => {{
            c.classList.remove("active");
            c.setAttribute("aria-pressed", "false");
          }});
          chip.classList.add("active");
          chip.setAttribute("aria-pressed", "true");

          const filter = chip.dataset.credFilter;
          accordionItems.forEach(item => {{
            const topics = (item.dataset.topics || "").toLowerCase().split(" ");
            if (filter === "all" || topics.includes(filter)) {{
              item.classList.remove("hidden");
            }} else {{
              item.classList.add("hidden");
            }}
          }});
        }});
      }});

      /* -----------------------------------------------------------
         7. FORM-FREE APPLICATION BUILDER & LIVE MESSAGE GENERATOR
         ----------------------------------------------------------- */
      const applyNameInput = document.getElementById("applyName");
      const applyNotesInput = document.getElementById("applyNotes");
      const applyMessageOutput = document.getElementById("applyMessageOutput");
      const copyMessageBtn = document.getElementById("copyMessageBtn");
      const copyStatusLine = document.getElementById("copyStatusLine");

      const builderState = {{
        name: "",
        goal: "",
        experience: "",
        injuries: "",
        location: "",
        notes: ""
      }};

      function updateGeneratedMessage() {{
        const nameDisplay = builderState.name.trim() || "[your name]";
        const goalDisplay = builderState.goal || "[selected goal]";
        const expDisplay = builderState.experience || "[training experience]";
        const injDisplay = builderState.injuries || "[injuries or pain]";
        const locDisplay = builderState.location || "[gym / home]";
        
        let msg = `Hi coach, I'm ${{nameDisplay}} and I'd like to apply for online coaching.\\n\\n`;
        msg += `Main goal: ${{goalDisplay}}\\n`;
        msg += `Training experience: ${{expDisplay}}\\n`;
        msg += `Injuries or pain: ${{injDisplay}}\\n`;
        msg += `I train at: ${{locDisplay}}`;

        if (builderState.notes.trim()) {{
          msg += `\\nAdditional notes: ${{builderState.notes.trim()}}`;
        }}

        applyMessageOutput.value = msg;
      }}

      applyNameInput.addEventListener("input", (e) => {{
        builderState.name = e.target.value;
        updateGeneratedMessage();
      }});
      applyNotesInput.addEventListener("input", (e) => {{
        builderState.notes = e.target.value;
        updateGeneratedMessage();
      }});

      document.querySelectorAll("[data-builder-group]").forEach(group => {{
        const groupKey = group.dataset.builderGroup;
        const chips = group.querySelectorAll(".b-chip");

        chips.forEach(chip => {{
          chip.addEventListener("click", () => {{
            const isSelected = chip.getAttribute("aria-pressed") === "true";
            chips.forEach(c => c.setAttribute("aria-pressed", "false"));
            if (!isSelected) {{
              chip.setAttribute("aria-pressed", "true");
              builderState[groupKey] = chip.dataset.val;
            }} else {{
              builderState[groupKey] = "";
            }}
            updateGeneratedMessage();
          }});
        }});
      }});

      updateGeneratedMessage();

      function copyApplicationToClipboard(callback) {{
        const textToCopy = applyMessageOutput.value;
        if (!textToCopy) return;

        function showSuccess() {{
          copyStatusLine.textContent = "✓ Application message copied! Ready to paste & send.";
          setTimeout(() => {{
            copyStatusLine.textContent = "";
          }}, 5000);
          if (callback) callback();
        }}

        if (navigator.clipboard && window.isSecureContext) {{
          navigator.clipboard.writeText(textToCopy).then(() => {{
            showSuccess();
          }}).catch(() => {{
            fallbackCopy();
          }});
        }} else {{
          fallbackCopy();
        }}

        function fallbackCopy() {{
          applyMessageOutput.select();
          applyMessageOutput.setSelectionRange(0, 99999);
          try {{
            document.execCommand("copy");
            showSuccess();
          }} catch (err) {{
            copyStatusLine.textContent = "Please select the text box and copy.";
            if (callback) callback();
          }}
        }}
      }}

      copyMessageBtn.addEventListener("click", () => {{
        copyApplicationToClipboard();
      }});

      /* Auto-copy and navigate when clicking social buttons */
      const sendInstagramBtn = document.getElementById("sendInstagramBtn");
      const sendFacebookBtn = document.getElementById("sendFacebookBtn");

      if (sendInstagramBtn) {{
        sendInstagramBtn.addEventListener("click", () => {{
          copyApplicationToClipboard();
        }});
      }}
      if (sendFacebookBtn) {{
        sendFacebookBtn.addEventListener("click", () => {{
          copyApplicationToClipboard();
        }});
      }}

      /* -----------------------------------------------------------
         8. FLOATING ACTION PILL (Appears on scroll past Hero)
         ----------------------------------------------------------- */
      const floatingApplyBtn = document.getElementById("floatingApplyBtn");
      const heroSection = document.getElementById("hero");

      window.addEventListener("scroll", () => {{
        if (!floatingApplyBtn || !heroSection) return;
        const heroBottom = heroSection.getBoundingClientRect().bottom;
        if (heroBottom < 100) {{
          floatingApplyBtn.classList.add("visible");
        }} else {{
          floatingApplyBtn.classList.remove("visible");
        }}
      }}, {{ passive: true }});

      /* -----------------------------------------------------------
         9. GIANT FOOTER WORDMARK WITH LETTER ROLL & CONTAINER FIT
         Row 1: "Karlsthetics" (left-aligned)
         Row 2: "Fitness" (right-aligned beneath it at the same size)
         ----------------------------------------------------------- */
      const wordmarkWrap = document.getElementById("wordmarkWrap");
      const wordmarkRow1 = document.getElementById("wordmarkRow1");
      const wordmarkRow2 = document.getElementById("wordmarkRow2");

      const word1 = "Karlsthetics";
      const word2 = "Fitness";

      function createLetterRoll(char) {{
        const span = document.createElement("span");
        span.className = "roll-letter";
        span.tabIndex = 0;
        span.setAttribute("aria-hidden", "true");

        const inner = document.createElement("span");
        inner.className = "roll-letter-inner";

        const primaryGlyph = document.createElement("span");
        primaryGlyph.className = "roll-glyph";
        primaryGlyph.textContent = char;

        const altGlyph = document.createElement("span");
        altGlyph.className = "roll-glyph glyph-alt";
        altGlyph.textContent = char;

        inner.appendChild(primaryGlyph);
        inner.appendChild(altGlyph);
        span.appendChild(inner);

        span.addEventListener("click", () => {{
          span.classList.toggle("toggled");
        }});
        span.addEventListener("keydown", (e) => {{
          if (e.key === "Enter" || e.key === " ") {{
            e.preventDefault();
            span.classList.toggle("toggled");
          }}
        }});

        return span;
      }}

      wordmarkRow1.innerHTML = "";
      wordmarkRow2.innerHTML = "";

      for (let char of word1) {{
        wordmarkRow1.appendChild(createLetterRoll(char));
      }}
      for (let char of word2) {{
        wordmarkRow2.appendChild(createLetterRoll(char));
      }}

      function fitWordmark() {{
        const containerWidth = wordmarkWrap.clientWidth;
        if (!containerWidth) return;

        let low = 20;
        let high = 450;
        let best = low;

        for (let i = 0; i < 18; i++) {{
          const mid = (low + high) / 2;
          wordmarkRow1.style.fontSize = `${{mid}}px`;
          if (wordmarkRow1.scrollWidth <= containerWidth) {{
            best = mid;
            low = mid;
          }} else {{
            high = mid;
          }}
        }}

        const finalSize = Math.floor(best);
        wordmarkRow1.style.fontSize = `${{finalSize}}px`;
        wordmarkRow2.style.fontSize = `${{finalSize}}px`;
      }}

      window.addEventListener("resize", fitWordmark);

      if (document.fonts && document.fonts.ready) {{
        document.fonts.ready.then(fitWordmark);
      }} else {{
        setTimeout(fitWordmark, 500);
      }}
      fitWordmark();
    }});
  </script>
</body>
</html>
'''

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

with open("generate_portfolio.py", "w", encoding="utf-8") as f:
    f.write(f'''# Regenerated portfolio script
{html_template}
''')

print("Updated index.html and generate_portfolio.py successfully without the target calculator!")
