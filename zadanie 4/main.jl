using Pkg
Pkg.add("HTTP")
Pkg.add("JSON")
using HTTP
using JSON
function weather_request(name)
  weather_key = ENV["WEATHER_KEY"]
  request = HTTP.request("GET", "http://api.weatherapi.com/v1/current.json?key=$(weather_key)&q=$(name)&aqi=no")
  result = String(request.body)
  json_result = JSON.parse(result)
  temp_c = json_result["current"]["temp_c"]
  temp_k = temp_c + 273.15
  location_name = json_result["location"]["name"]
  println("Temperatura dla $(location_name):")
  println("$(temp_k) K")
end
weather_request("London")
weather_request("Warsaw")
weather_request("New_York")