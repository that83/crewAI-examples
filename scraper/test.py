import re

def remove_duplicate_urls(input_string):
    lines = input_string.split('\n')
    seen_urls = set()
    result_lines = []
    
    url_pattern = re.compile(r'http[s]?://\S+')
    
    for line in lines:
        match = url_pattern.search(line)
        if match:
            url = match.group(0)
            if url not in seen_urls:
                seen_urls.add(url)
                result_lines.append(line)
        else:
            result_lines.append(line)
    
    return '\n'.join(result_lines)

# Example usage
input_string = """
      Purpose of this process is to scrape the data from the search result urls and save it to a file.

      Step 0: Use a scraping tool to extract data from the search result urls. In this step, scraping tool will also save the scraped data to file.
      Search result urls: Here are the search results for the provided search phrases:

1. **"Jewish parenting methods site:reddit.com"**
   - [Hello Israel! I am curious how Jews/Israeli parenting is. For ...](https://www.reddit.com/r/Israel/comments/cwgnxl/hello_israel_i_am_curious_how_jewsisraeli/)
   - [r/Judaism - Boker tov! Do y'all have any Jewish pregnancy ...](https://www.reddit.com/r/Judaism/comments/y90sci/boker_tov_do_yall_have_any_jewish_pregnancy_andor/)
   - [Jewish Culture for pregnancy, childbirth, postpartum, & ...](https://www.reddit.com/r/Judaism/comments/ewoykx/jewish_culture_for_pregnancy_childbirth/)
   - [Jewish moms : r/Jewish](https://www.reddit.com/r/Jewish/comments/18aekvy/jewish_moms/)
   - [Quick Question; What do parents do over Shabbat?](https://www.reddit.com/r/Judaism/comments/14ghulm/quick_question_what_do_parents_do_over_shabbat/)
   - [Girls raised by Jewish parents are 23 percentage points ...](https://www.reddit.com/r/science/comments/u8cf44/girls_raised_by_jewish_parents_are_23_percentage/)
   - [Why do religious Jews have so many kids? : r/Judaism](https://www.reddit.com/r/Judaism/comments/168k86/why_do_religious_jews_have_so_many_kids/)
   - [Jewish parenting : r/tumblr](https://www.reddit.com/r/tumblr/comments/12pmpc8/jewish_parenting/)
   - [What is Israeli parenting style like ? : r/Israel](https://www.reddit.com/r/Israel/comments/4nltqy/what_is_israeli_parenting_style_like/)
   - [Jewish vs Russian vs Asian parenting](https://www.reddit.com/r/AsianParentStories/comments/1ddpqx9/jewish_vs_russian_vs_asian_parenting/)

2. **"How Jewish parents educate their children site:reddit.com"**
   - [How do jewish families raise their children?](https://www.reddit.com/r/Jewish/comments/1cvb1ou/how_do_jewish_families_raise_their_children/)
   - [Education Culture : r/Judaism](https://www.reddit.com/r/Judaism/comments/1aidr1s/education_culture/)
   - [Raising a Jewish child when we are not Jewish : r/Judaism](https://www.reddit.com/r/Judaism/comments/w2itwt/raising_a_jewish_child_when_we_are_not_jewish/)
   - [Atheist Jews who have/are raising children - how did you ...](https://www.reddit.com/r/ReformJews/comments/14kx1xc/atheist_jews_who_haveare_raising_children_how_did/)
   - [Parents, how are you dealing with the Jewish value on ...](https://www.reddit.com/r/Judaism/comments/1bqxivs/parents_how_are_you_dealing_with_the_jewish_value/)
   - [Is there a Jewish way of raising your children? : r/Israel](https://www.reddit.com/r/Israel/comments/m6aukc/is_there_a_jewish_way_of_raising_your_children/)
   - [Do you think that Jewish parents put as much pressure to ...](https://www.reddit.com/r/Jewish/comments/tz6uti/do_you_think_that_jewish_parents_put_as_much/)
   - [Jewish Parenting Advice : r/Judaism](https://www.reddit.com/r/Judaism/comments/10q70c0/jewish_parenting_advice/)
   - [Raising a proud Jewish child : r/Judaism](https://www.reddit.com/r/Judaism/comments/1dt0rgz/raising_a_proud_jewish_child/)
   - [How do I raise a child Jewish in a rural non Jewish area?](https://www.reddit.com/r/Judaism/comments/mzbd3p/how_do_i_raise_a_child_jewish_in_a_rural_non/)

3. **"Jewish child-rearing practices site:reddit.com"**
   - [Jewish Culture for pregnancy, childbirth, postpartum, & ...](https://www.reddit.com/r/Judaism/comments/ewoykx/jewish_culture_for_pregnancy_childbirth/
   - [Why do religious Jews have so many kids? : r/Judaism](https://www.reddit.com/r/Judaism/comments/168k86/why_do_religious_jews_have_so_many_kids/)
   - [My son is convinced we are Jewish : r/Parenting](https://www.reddit.com/r/Parenting/comments/zqyh3g/my_son_is_convinced_we_are_jewish/)
   - [Girls raised by Jewish parents are 23 percentage points ...](https://www.reddit.com/r/science/comments/u8cf44/girls_raised_by_jewish_parents_are_23_percentage/)
   - [How do parents practice? : r/Hellenism](https://www.reddit.com/r/Hellenism/comments/14sb57x/how_do_parents_practice/)
   - [Jewish OAD Families? : r/oneanddone](https://www.reddit.com/r/oneanddone/comments/18g0wlo/jewish_oad_families/)
   - [Jewish parenting : r/tumblr](https://www.reddit.com/r/tumblr/comments/12pmpc8/jewish_parenting/)
   - [Jewish mom of daughter who might be raised non- ...](https://www.reddit.com/r/Judaism/comments/1ejfj1x/jewish_mom_of_daughter_who_might_be_raised/)
   - [Interfaith marriage with baby on the way... unexpected ...](https://www.reddit.com/r/Parenting/comments/6875jl/interfaith_marriage_with_baby_on_the_way/)
   - [What do you do as a mom raising a patrilineal Jew alone?](https://www.reddit.com/r/Jewish/comments/1bn0sok/what_do_you_do_as_a_mom_raising_a_patrilineal_jew/)

4. **"Jewish education for kids site:reddit.com"**
   - [How am I supposed to afford jewish school for my future ...](https://www.reddit.com/r/Judaism/comments/1d87erf/how_am_i_supposed_to_afford_jewish_school_for_my/)
   - [Chabad has led to a diminution of Jewish education... ...](https://www.reddit.com/r/ReformJews/comments/1b94aof/chabad_has_led_to_a_diminution_of_jewish/)
   - [Successful models of Jewish education : r/Judaism](https://www.reddit.com/r/Judaism/comments/13o7suv/successful_models_of_jewish_education/)
   - [Is Jewish day school better than public school? : r/Judaism](https://www.reddit.com/r/Judaism/comments/1cvq7tj/is_jewish_day_school_better_than_public_school/)
   - [On a scale of 1-10, how important is Jewish learning/ ...](https://www.reddit.com/r/Judaism/comments/1cx9hiw/on_a_scale_of_110_how_important_is_jewish/)
   - [Hebrew or Israeli baby/toddler/children educational content ...](https://www.reddit.com/r/Judaism/comments/1bpukht/hebrew_or_israeli_babytoddlerchildren_educational/)
   - [What do you wish was taught in Hebrew School? : r/Judaism](https://www.reddit.com/r/Judaism/comments/14wubdy/what_do_you_wish_was_taught_in_hebrew_school/)
   - [When to Start Hebrew School? : r/Judaism](https://www.reddit.com/r/Judaism/comments/16cycz3/when_to_start_hebrew_school/)
   - [Education Culture : r/Judaism](https://www.reddit.com/r/Judaism/comments/1aidr1s/education_culture/)
   - [How do jewish families raise their children?](https://www.reddit.com/r/Jewish/comments/1cvb1ou/how_do_jewish_families_raise_their_children/)

"""

output_string = remove_duplicate_urls(input_string)
print(output_string)