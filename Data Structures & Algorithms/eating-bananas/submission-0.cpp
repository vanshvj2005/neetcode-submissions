class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int s = 1;
        int e = *max_element(piles.begin(), piles.end());

        int ans = e;

        while(s <= e) {

            int mid = s + (e - s) / 2;

            long long totalHours = 0;

            for(int i = 0; i < piles.size(); i++) {
                totalHours += ceil((double)piles[i] / mid);
            }

            if(totalHours <= h) {
                ans = mid;
                e = mid - 1;
            }
            else {
                s = mid + 1;
            }
        }

        return ans;
    }
};