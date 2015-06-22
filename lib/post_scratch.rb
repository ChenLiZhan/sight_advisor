require 'nokogiri'
require 'open-uri'
require 'concurrent'
require 'yaml'
require 'csv'

TRIPADVISOR_BASE = 'http://www.tripadvisor.com.tw'
TRIPADVISOR_TAITUNG = 'http://www.tripadvisor.com.tw/Attractions-g304163-Activities-Taitung.html'

POST_LINK_XPATH = "//div[@class = 'property_title']//a/@href"
REVIEWS_LINK_XPATH = "//div[@class = 'wrap']//div[@class = 'quote']//a/@href"
REVIEW_TITLE_XPATH = "//div[@class = 'quote']"
REVIEW_CONTENT_XPATH = "//div[@class = 'entry']//p"
SIGHT_ADDRESS_XPATH = "//span[@class= 'format_address']//span"
SIGHT_NAME_XPATH = "//ul[@class = 'breadcrumbs']/li"
PAGE_XPATH = "//div[@class = 'pageNumbers']"
PAGE_LINK_XPATH = "//div[@class = 'pageNumbers']//@href"

# REVIEWS_TITLE = "//div[@class = 'wrap']//div[@class = 'quote']//a//span"
# reviews_page = Nokogiri::HTML(open('http://www.tripadvisor.com.tw/Attraction_Review-g304163-d2087111-Reviews-Orchid_Island-Taitung.html'))
# address = reviews_page.xpath(SIGHT_ADDRESS_XPATH)
# name = reviews_page.xpath(SIGHT_NAME_XPATH).last.content
# pages = reviews_page.xpath(PAGE_XPATH)
# reviews = reviews_page.xpath(REVIEWS_TITLE)
# reviews.each do |review|
#     record = {
#         'sight'     => name,
#         'review'    => review.content
#     }
#     puts record
# end
# unless pages.empty?
#     pages_link = reviews_page.xpath(PAGE_LINK_XPATH)
#     pages_link.each do |page|
#         certain_page = Nokogiri::HTML(open(TRIPADVISOR_BASE + page.value))
#         reviews = certain_page.xpath(REVIEWS_LINK_XPATH)
#         reviews.each do |review|
#             comment_page = Nokogiri::HTML(open(TRIPADVISOR_BASE + review.content))
#             title = comment_page.xpath(REVIEW_TITLE_XPATH)[0].content
#             content = comment_page.xpath(REVIEW_CONTENT_XPATH)[0].content
#             record = {
#                 'sight'     => name,
#                 'title'     => title,
#                 'content'   => content
#             }

#             puts record
#         end
#     end
# end

all_sights = []

document = Nokogiri::HTML(open(TRIPADVISOR_TAITUNG))
sights_link = document.xpath(POST_LINK_XPATH)

sights_link.each do |sight|
    reviews_page = Nokogiri::HTML(open(TRIPADVISOR_BASE + sight))
    address = reviews_page.xpath(SIGHT_ADDRESS_XPATH)
    name = reviews_page.xpath(SIGHT_NAME_XPATH).last.content
    pages = reviews_page.xpath(PAGE_XPATH)
    reviews = reviews_page.xpath(REVIEWS_LINK_XPATH)
    reviews.each do |review|
        comment_page = Nokogiri::HTML(open(TRIPADVISOR_BASE + review.content))
        title = comment_page.xpath(REVIEW_TITLE_XPATH)[0].content
        content = comment_page.xpath(REVIEW_CONTENT_XPATH)[0].content
        record = {
            'sight'     => name,
            'title'     => title,
            'content'   => content
        }
        all_sights << record
        puts record
    end
    unless pages.empty?
        pages_link = reviews_page.xpath(PAGE_LINK_XPATH)
        pages_link.each do |page|
            certain_page = Nokogiri::HTML(open(TRIPADVISOR_BASE + page))
            reviews = certain_page.xpath(REVIEWS_LINK_XPATH)
            reviews.each do |review|
                comment_page = Nokogiri::HTML(open(TRIPADVISOR_BASE + review.content))
                title = comment_page.xpath(REVIEW_TITLE_XPATH)[0].content
                content = comment_page.xpath(REVIEW_CONTENT_XPATH)[0].content
                record = {
                    'sight'     => name,
                    'title'     => title,
                    'content'   => content
                }
                all_sights << record
                puts record
            end
        end
    end
end

CSV.open("sight.csv", "wb") do |csv|
  csv << ['sight', 'title', 'content']
  all_sights.each do |sight|
    csv << [sight['sight'], sight['title'], sight['content']]
  end
end
# File.open('sight.yml', 'w') do |file|
#     file.write(all_sights.to_yaml)
# end
