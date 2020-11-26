'''
Jeremy Tandjung
Assignment3 - Log Analysis
CSS 390 - Scripting Language
Morris Bernstein
'''


import sys

# get the Segmentest_segment_dict Dictionary and Cookie Dictionary
def getLogAnalysis(filename: str):
    f = open(filename)
    cDict = {}
    sDict = {}

    cCount = 0
    csegCount = 0
    for line in f:
        if 'evaluated' in line:
            cCount += 1
            lArr = line.split('==>')
            cookie = lArr[0].split(':')[-1][1:-1]
            segmentest_segment_dict = lArr[-1][1:-1]

            segArr = []
            if segmentest_segment_dict != '[]':
                csegCount += 1
                segArr = segmentest_segment_dict.split(',')
                segArr = [seg.strip(' ') for seg in segArr]
                segArr = [seg.strip('[') for seg in segArr]
                segArr = [seg.strip(']') for seg in segArr]


            for seg in segArr:
                #add segment key if doesn't exist in sDict
                if seg not in sDict.keys():
                    sDict.update({seg: []})
                sDict[seg].append(cookie)
            #print(segArr)
            c_seg = {cookie: segArr}
            cDict.update(c_seg)
    #print(cDict)
    f.close()
    return cDict, sDict

def countEmpty(d: dict) -> int:
    ans = 0
    for k in d.keys():
        if len(d[k]) == 0:
            ans += 1
    return ans

def getEmpty(d: dict) -> list:
    ans = []
    for k in d.keys():
        if len(d[k]) == 0: #if empty
            ans.append(k)
    return ans


def getDifferent(checkHere, fromHere):
    ans = {}

    for k in checkHere.keys():
        arr = []
        if k in fromHere.keys():
            for val in checkHere[k]:
                if val not in fromHere[k]: #check if val exist in the other array
                    arr.append(val)
        if len(arr) > 0:
            ans.update({k: arr})
    return ans


def stringDict(d):
    i = 0
    ans = ''
    for k in sorted(d.keys()):
        ans += ('%d\t%s\t%d\t%s\n' % (i, k, len(d[k]), d[k]))
        i += 1
    ans += '\n'
    return ans


def getReport(baseline: str, test: str):
    baseline_cookie_dict, baseline_segment_dict = getLogAnalysis(baseline)
    test_cookie_dict, test_segment_dict = getLogAnalysis(test)

    b_emptyC, t_emptyC = getEmpty(baseline_cookie_dict), getEmpty(test_cookie_dict)

    # count empty cookie only in baseline
    b_ecCount = 0
    for c in b_emptyC:
        if c not in t_emptyC:
            b_ecCount += 1

    # count empty cookie only in test
    t_ecCount = 0
    for c in t_emptyC:
        if c not in b_emptyC:
            t_ecCount += 1

    eCBoth = (len(test_cookie_dict.keys()) - len(t_emptyC)) - t_ecCount
    eCEither = eCBoth + t_ecCount + b_ecCount

    # print('%d = %d' % (countEmpty(baseline_cookie_dict), len(b_emptyC)))
    # print('%d = %d' % (countEmpty(test_cookie_dict), len(t_emptyC)))

    summary = 'Summary:'

    summary += '\ntotal cookies in baseline =\t%d' % len(baseline_cookie_dict.keys())
    summary += '\nempty cookies in baseline =\t%d' % len(b_emptyC)
    summary += '\nnon-empty cookies in baseline =\t%d' % (len(baseline_cookie_dict.keys()) - len(b_emptyC))

    summary += '\ntotal cookies in test =\t %d' % len(test_cookie_dict.keys())
    summary += '\nempty cookies in test =\t %d' % len(t_emptyC)
    summary += '\nnon-empty cookies in test =\t%d' % (len(test_cookie_dict.keys()) - len(t_emptyC))

    summary += '\nnon-empty cookies in baseline only = \t%d' % b_ecCount
    summary += '\nnon-empty cookies in test only = \t%d' % t_ecCount
    summary += '\nnon-empty cookies in both = \t%d' % eCBoth
    summary += '\nnon-empty cookies in either = \t%d\n' % eCEither



    #addedSegment
    segmentPlus = getDifferent(test_segment_dict, baseline_segment_dict)
    summary += ('Cookies with added segmentest_segment_dict: %d / %d\n') % (len(segmentPlus), len(baseline_segment_dict))
    summary += stringDict(segmentPlus)

    #missingSegment
    segmentMinus = getDifferent(baseline_segment_dict, test_segment_dict)
    summary += ('Cookies with missing segmentest_segment_dict: %d / %d\n') % (len(segmentMinus), len(baseline_segment_dict))
    summary += stringDict(segmentMinus)

    #added cookies
    cookiePlus = getDifferent(test_cookie_dict, baseline_cookie_dict)
    summary += '\nSegmentest_segment_dict with added cookies: %d / %d\n' % (len(cookiePlus), len(test_cookie_dict))
    summary += stringDict(cookiePlus)


    #missing cookies
    cookieMinus = getDifferent(baseline_cookie_dict, test_cookie_dict)
    summary += 'Segment with missing cookies: %d / %d\n' % (len(cookieMinus), len(test_cookie_dict))
    summary += stringDict(cookieMinus)

    #print(baseline_segment_dict)
    #print(test_segment_dict)
    print(summary)


#testFile = 'evaluator-integration.log'
#baselineFile = 'evaluator-integration-baseline.log'

if __name__ == '__main__':
    baseline = sys.argv[1]
    test = sys.argv[2]
    getReport(baseline, test)

testFile = 'test.log'
baselineFile = 'baseline.log'


#added cookies
