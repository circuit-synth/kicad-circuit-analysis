# CLAUDE.md - kicad-circuit-analysis

This file provides guidance to Claude Code when working on the kicad-circuit-analysis project.

## Project Overview

**kicad-circuit-analysis** is a professional Python library for quality assurance and failure mode analysis of KiCAD circuit designs. It provides AI-powered FMEA analysis, comprehensive design validation, and professional reporting capabilities.

## Key Features

- **AI-Powered FMEA**: Comprehensive failure mode and effects analysis using ML models
- **Risk Assessment**: Quantitative risk scoring with uncertainty analysis  
- **Circuit Validation**: Deep analysis of schematic and PCB designs
- **Professional Reports**: Publication-ready analysis reports (PDF, Excel, JSON)
- **MCP Integration**: Native AI agent integration via Model Context Protocol
- **Component Intelligence**: Library of failure modes and best practices

## Project Structure

```
kicad-circuit-analysis/
├── python/                          # Core Python library
│   ├── kicad_circuit_analysis/
│   │   ├── core/                   # Core analysis engine
│   │   │   └── circuit_parser.py   # KiCAD file parser
│   │   ├── fmea/                    # FMEA analysis modules
│   │   │   ├── fmea_analyzer.py           # Basic FMEA
│   │   │   ├── enhanced_fmea_analyzer.py  # AI-enhanced FMEA
│   │   │   └── comprehensive_fmea_report_generator.py
│   │   ├── analysis/               # Analysis algorithms
│   │   ├── mcp/                     # MCP server interface
│   │   │   └── server.py           # MCP server
│   │   ├── utils/                   # Utilities and helpers
│   │   └── cli.py                   # Command line interface
│   ├── examples/                    # Usage examples
│   └── tests/                       # Test suite
├── mcp-server/                      # TypeScript MCP server
└── README.md
```

## Development Commands

```bash
# Install dependencies
cd python && pip install -e ".[dev]"

# Run FMEA analysis
kicad-fmea circuit.kicad_sch --ai --output report.pdf

# Run quality assurance
kicad-qa project.kicad_pro --checks electrical thermal

# Run tests
cd python && pytest

# Build package
cd python && python -m build
```

## Core API Usage

```python
import kicad_circuit_analysis as kca

# FMEA Analysis
analyzer = kca.FMEAAnalyzer()
analyzer.load_schematic('circuit.kicad_sch')
report = analyzer.run_comprehensive_fmea(ai_enhanced=True)

# Quality Assurance
qa = kca.QualityAssurance()
results = qa.analyze_design('project.kicad_pro')
risk_score = qa.calculate_risk_score(results)
```

## AI Integration

The library includes advanced AI features:

- **Failure Prediction**: ML models for component failure analysis
- **Risk Quantification**: Probabilistic assessment with confidence intervals
- **Design Optimization**: AI-suggested improvements
- **Expert Knowledge**: Curated failure mode database

## Analysis Types

1. **Electrical Analysis**: 
   - Power integrity checks
   - Signal integrity validation
   - EMC/EMI assessment

2. **Thermal Analysis**:
   - Power dissipation analysis
   - Thermal runaway detection
   - Junction temperature estimation

3. **Mechanical Analysis**:
   - Stress analysis for components
   - Vibration susceptibility
   - Thermal expansion effects

4. **Manufacturing Analysis**:
   - DFM (Design for Manufacturing) checks
   - Assembly process validation
   - Test coverage assessment

## MCP Integration

The package provides MCP server capabilities:

- **Python MCP**: `kicad-analysis-mcp` command
- **TypeScript MCP**: Full-featured server with Python integration

## Development Notes

- **Quality Focus**: Professional-grade analysis suitable for production
- **AI Integration**: Leverages latest ML models for enhanced insights
- **Report Generation**: Publication-ready documentation
- **Standards Compliance**: Follows industry FMEA standards
- **Extensible**: Plugin architecture for custom analysis modules

## Dependencies

- `kicad-sch-api`: Schematic file parsing
- `kicad-pcb-api`: PCB file analysis  
- `pandas`: Data analysis and reporting
- `numpy`: Numerical computations
- `loguru`: Advanced logging

## Related Projects

- **kicad-sch-api**: Schematic manipulation library
- **kicad-pcb-api**: PCB manipulation library
- **engineering-memory-bank**: AI-powered decision documentation
- **circuit-synth**: Main circuit design automation project

---

*This repository is part of the Circuit-Synth professional ecosystem*