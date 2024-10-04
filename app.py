from iebank_api import app
import os

# original code (uses port 5000 by default)
#if __name__ == '__main__':
    # app.run(debug=True)

# new code (uses port 80)
if __name__ == '__main__':
    port_to_use = int(os.environ.get('FLASK_RUN_PORT', 5000))  # Default to 5000 if FLASK_RUN_PORT is not set
    app.run(host='0.0.0.0', port=port_to_use , debug=True)