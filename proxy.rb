require 'sinatra'
require 'httparty'
require 'json'

set :port, ENV['PORT'] || 4567
set :bind, '0.0.0.0'

get '/toad64' do
  url = "https://ch.tetr.io/api/users/toad64"
  response = HTTParty.get(url)
  content_type :json
  response.body
end