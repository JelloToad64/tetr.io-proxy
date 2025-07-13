set :port, ENV['PORT'] || 4567
set :bind, '0.0.0.0'

require "sinatra"
require "httparty"

set :port, ENV.fetch("PORT", 4567)
set :bind, "0.0.0.0"

before do
  content_type "application/json"
  headers "Access-Control-Allow-Origin" => "*"
end

get "/tetrio/:username" do
  response = HTTParty.get("https://ch.tetr.io/api/users/toad64")
  status response.code
  body response.body
end
