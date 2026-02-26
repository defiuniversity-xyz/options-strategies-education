# Options Strategies: Statistical Edge Analysis

A single-page educational web application covering the quantitative mechanics, statistical edge, risk management, and capital efficiency of systematic options trading strategies.

## Live Site

[options-strategies-edu.web.app](https://options-strategies-edu.web.app)

## Strategies Covered

- **Short Strangles & Straddles** — Volatility Risk Premium + theta decay harvest
- **Jade Lizards & Twisted Sisters** — Volatility skew anomaly exploitation
- **Iron Condors & Iron Butterflies** — Defined-risk VRP harvesting (IRA-friendly)
- **Broken Wing Butterfly** — Asymmetric credit-routed premium collection
- **Calendar & Diagonal Spreads** — Term structure and vega expansion plays
- **Naked Puts & Covered Strangles** — Equity-blended VRP yield generation

## Key Features

- Dark financial UI with Inter typography
- Sticky sidebar navigation with scroll-spy highlighting
- Interactive tabbed content panels for each strategy
- Inline SVG payoff diagrams for every strategy
- Color-coded strategy comparison matrix
- Fully responsive (mobile hamburger menu)
- Self-contained single `index.html` — no build tools or dependencies

## Foundational Concepts

- Volatility Risk Premium (VRP): 19.3% avg IV vs 15.1% avg RV (1990–2018) = 4.2pp persistent edge
- Theta decay acceleration in the 45→21 DTE window
- Implied volatility mean reversion and IV Rank (IVR) signals

## Hosting

Deployed on Firebase Hosting (free Spark plan).

```bash
firebase deploy
```

## Sources

Key academic and industry sources include the Cboe CNDR/BFLY Index 35-year studies, the Cboe PutWrite (PUT) Index 32-year historical analysis, Princeton Dataspace VRP research, and OCC TIMS Portfolio Margin methodology documentation.
