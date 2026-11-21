"""Launch MatchLab in dev mode with hot logging."""
import sys
from src.main.process import bootstrap

if __name__ == "__main__":
    sys.exit(bootstrap(sys.argv))