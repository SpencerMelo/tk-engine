import math

from durable.lang import *

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
numbers = '0 1 2 3 4 5 6 7 8 9'
special_chars = '! ” # $ % & ’ ) ( * + , - . / : ; < = > ? @ ] [ \\ ^'


def print_bounds(text, limit):
    limit = int(limit)
    print(text.format(limit - 1, limit, limit + 1))


with ruleset('input'):
    @when_all((m.type == 'text')
              & ((m.restrictions.anyItem(item == 'none'))
                 | (m.restrictions.anyItem(item == 'numeric')))
              | (m.type == 'number'))
    def numeric(c):
        print('For happy path, test with at least one of: ' + numbers)

    @when_all((m.type == 'text')
              & ((m.restrictions.anyItem(item == 'none'))
                 | (m.restrictions.anyItem(item == 'alphabetical'))
                 & (m.restrictions.anyItem(item == 'lowercase'))))
    def alphabetical_lower(c):
        print('For happy path, test with at least one of: ' + alphabet)

    @when_all((m.type == 'text')
              & ((m.restrictions.anyItem(item == 'none'))
                 | (m.restrictions.anyItem(item == 'alphabetical'))
                 & (m.restrictions.anyItem(item == 'uppercase'))))
    def alphabetical_upper(c):
        print('For happy path, test with at least one of: ' + alphabet.upper())

    @when_all((m.type == 'text')
              & ((m.restrictions.anyItem(item == 'none'))
                 | (m.restrictions.anyItem(item == 'special_character'))))
    def special_character(c):
        print('For happy path, test with at least one of: ' + special_chars)

    @when_all((m.type == 'text')
              & (m.restrictions.anyItem(item == 'numeric'))
              & (m.restrictions.allItems(item != 'alphabetical'))
              | (m.type == 'number'))
    def numeric_only(c):
        print('For unhappy path, test with letters.')

    @when_all((m.type == 'text')
              & ((m.restrictions.anyItem(item == 'alphabetical'))
                 & (m.restrictions.allItems(item != 'uppercase'))
                 & (m.restrictions.anyItem(item == 'lowercase'))))
    def alphabetical_lower_only(c):
        print('For unhappy path, test with uppercase letters.')

    @when_all((m.type == 'text')
              & ((m.restrictions.anyItem(item == 'alphabetical'))
                 & (m.restrictions.allItems(item != 'lowercase'))
                 & (m.restrictions.anyItem(item == 'uppercase'))))
    def alphabetical_upper_only(c):
        print('For unhappy path, test with lowercase letters.')

    @when_all((m.type == 'text')
              & ((m.restrictions.anyItem(item == 'alphabetical'))
                 & (m.restrictions.allItems(item != 'numeric'))))
    def alphabetical_only(c):
        print('For unhappy path, test with any number.')

    @when_all(m.min != '')
    def min_bound(c):
        text = ''
        if c.m.type == 'number':
            text = 'For minimum bounds, test with the values [{0}, {1}, {2}].'
        elif c.m.type == 'text':
            text = 'For minimum bounds, test with [{0}, {1}, {2}] digits.'
        print_bounds(text, c.m.min)

    @when_all(m.max != '')
    def max_bound(c):
        text = ''
        if c.m.type == 'number':
            text = 'For maximum bounds, test with the values [{0}, {1}, {2}].'
        elif c.m.type == 'text':
            text = 'For maximum bounds, test with [{0}, {1}, {2}] digits.'
        print_bounds(text, c.m.max)

with ruleset('form'):

    @when_all(m.type == 'static')
    def static_behavior(c):
        print('Left all fields empty and click on {0}.'.format(c.m.input))

    @when_all(m.type == 'dynamic')
    def dynamic_behavior(c):
        print('The \'{0}\' should be disabled by default.'.format(c.m.input))


    @when_all(m.required_fields > 0)
    def required_fields(c):
        print('Fill one \'required\' field and click on \'{0}\'.'.format(
            c.m.input))

        print('Fill all \'required\' fields and click on \'{0}\'.'.format(
            c.m.input))

    @when_all(m.normal_fields > 0)
    def normal_fields(c):
        print('Fill one \'normal\' field and click on \'{0}\'.'.format(
            c.m.input))
        print('Fill all \'normal\' fields and click on \'{0}\'.'.format(
            c.m.input))

with ruleset('sorting'):
    @when_all(m.order == 'asc')
    def asc(c):
        print('The higher value should be at the end of the page.')
        c.assert_fact({'order': m.order, 'datatype': m.datatype})


    @when_all(m.order == 'desc')
    def desc(c):
        print('The lowest value should be at the end of the page.')
        c.assert_fact({'order': m.order, 'datatype': m.datatype})

    @when_all(m.datatype == 'string')
    def string(c):
        print('Consider the length, scenarios like \'012 > 34\' might occur.')

    @when_all(m.datatype == 'date')
    def date(c):
        print('Consider the format, scenarios like \'20/01/20 > 19/08/20\' '
              'might happen in dd/mm/yy format.')

    @when_all(m.datatype == 'number')
    def string(c):
        print('No special rules for numbers, just check the proper order.')

with ruleset('pagination'):
    @when_all(m.total_pages > 0)
    def pagination(c):
        pages_expected = math.ceil(c.m.total_records / c.m.records_per_page)

        if pages_expected == c.m.total_pages:
            c.assert_fact({
                'remainder': c.m.total_records % c.m.records_per_page,
                'pages': c.m.total_pages,
                'records_per_page': c.m.records_per_page
            })
        else:
            print('Invalid amount of pages.')


    @when_all(m.remainder > 0)
    def remainder(c):
        text = 'On the last page, check if there is only {0} records there.'
        print(text.format(c.m.remainder))


    @when_all(m.remainder == 0)
    def no_remainder(c):
        text = 'Check if first, last and any other page has {0} records.'
        print(text.format(c.m.records_per_page))

    @when_all((m.hasNext == 'true') & (m.total_pages > 1))
    def next_button(c):
        print('On the last page, the next button should be disabled.')

    @when_all((m.hasPrevious == 'true') & (m.total_pages > 1))
    def previous_button(c):
        print('On the first page, the previous button should be disabled.')

    @when_all((m.hasNext == 'true')
              & (m.hasPrevious == 'true')
              & (m.total_pages == 1))
    def only_one_page(c):
        print('The next and previous button should be disabled.')

    @when_all(m.hasPageInput == 'true')
    def page_input(c):
        assert_fact('input', {
            'type': 'number',
            'restrictions': [],
            'min': '1',
            'max': str(c.m.total_pages),
        })

# tests

assert_fact('input', {
    'type': 'number',
    'restrictions': [
        'alphabetical',
        'lowercase'],
    'min': '6',
    'max': '10',
})

assert_fact('form', {
    'input': 'submit',
    'type': 'static',
    'required_fields': 5,
    'normal_fields': 3
})

assert_fact('sorting', {
    'order': 'asc',
    'datatype': 'string',
})

assert_fact('pagination', {
    'total_pages': 6,
    'records_per_page': 10,
    'total_records': 53,
    'hasNext': 'true',
    'hasPrevious': 'true',
    'hasPageInput': 'true'
})