# Context Portal Integration - kicad-circuit-analysis

## Setup

```bash
# Install Context Portal
cd tools/context-portal && pip install -e .

# Start server for this repository
uvx context-portal --workspace kicad-circuit-analysis --port 8003
```

## Repository Context

**kicad-circuit-analysis** provides professional quality assurance and FMEA analysis for KiCAD circuits.

### Key Development Areas

- **FMEA Analysis**: Failure mode and effects analysis algorithms
- **Risk Assessment**: Quantitative risk scoring methodologies
- **AI Integration**: Machine learning models for failure prediction
- **Report Generation**: Professional analysis documentation
- **Quality Workflows**: Engineering validation processes

### Context Categories

- `fmea-algorithms`: FMEA analysis approach decisions
- `risk-models`: Risk assessment and scoring methodologies  
- `ai-integration`: ML model choices and training approaches
- `reporting`: Professional report generation strategies
- `validation`: Quality assurance workflow patterns
- `knowledge-base`: Component failure mode databases

### Usage Examples

```bash
# Add context about FMEA methodology
uvx context-portal add --category fmea-algorithms "Simplified FMEA for v0.0.1 release"

# Query AI integration patterns
uvx context-portal query "machine learning failure prediction"

# Search reporting strategies
uvx context-portal query "professional PDF report generation"
```

This enables AI assistants to understand the quality assurance domain and development patterns specific to circuit analysis.