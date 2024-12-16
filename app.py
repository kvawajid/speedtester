from flask import Flask, jsonify, render_template
import speedtest


app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test-speed', methods=['GET'])
def test_speed():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1e6  # Convert to Mbps
        upload_speed = st.upload() / 1e6      # Convert to Mbps
        ping = st.results.ping
        return jsonify({
            'download_speed': f"{download_speed:.2f} Mbps",
            'upload_speed': f"{upload_speed:.2f} Mbps",
            'ping': f"{ping:.2f} ms"
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
