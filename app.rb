require 'sinatra/base'
require 'sinatra/flash'
require 'httparty'
require 'json'

class SightAdvisorApp < Sinatra::Base
  enable :sessions
  register Sinatra::Flash

  # BASE_URL = 'http://localhost:4567'
  BASE_URL = 'https://sightadvisor.herokuapp.com'
  get '/' do
    @result = HTTParty.get("#{BASE_URL}/api/v1/keywords");
    erb :index
  end
  
  get '/api/v1/keywords' do
    content_type :json, 'charset' => 'utf-8'
    s = File.read(File.join('public', 'keyword.txt'))
    s
  end
end
