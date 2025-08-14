"""
Basic FMEA analysis example for kicad-circuit-analysis.

Shows how to run failure mode analysis on a KiCAD schematic.
"""

import kicad_circuit_analysis as kca

def main():
    # Initialize quality assurance
    qa = kca.QualityAssurance()
    
    # For demo purposes, create a mock analysis
    print("KiCAD Circuit Analysis - Basic FMEA Example")
    print("=" * 50)
    
    try:
        # This would normally load a real project file
        # qa.load_project('example_project.kicad_pro')
        
        # Mock analysis results for demonstration
        print("Simulating FMEA analysis...")
        
        # Example analysis results
        results = {
            'issues': [
                {'description': 'Missing decoupling capacitor near U1', 'severity': 'Medium'},
                {'description': 'Power trace width may be insufficient', 'severity': 'Low'},
                {'description': 'No reverse polarity protection', 'severity': 'High'},
            ],
            'components_analyzed': 15,
            'nets_checked': 8
        }
        
        risk_score = 45  # Mock risk score
        
        print(f"\nAnalysis Complete!")
        print(f"Components Analyzed: {results['components_analyzed']}")
        print(f"Nets Checked: {results['nets_checked']}")
        print(f"Overall Risk Score: {risk_score}/100")
        
        print(f"\nIssues Found ({len(results['issues'])}):")
        for i, issue in enumerate(results['issues'], 1):
            print(f"  {i}. [{issue['severity']}] {issue['description']}")
        
        print(f"\nRecommendations:")
        print(f"  1. Add 100nF decoupling capacitor within 5mm of U1")
        print(f"  2. Increase power trace width to minimum 0.5mm")
        print(f"  3. Consider adding Schottky diode for reverse protection")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()