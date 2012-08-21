This permission map was built by Adrienne Porter Felt, Erika Chin, and Steve
Hanna at the University of California, Berkeley.

	Contact: android@eecs.berkeley.edu
	Website: www.android-permissions.org

We welcome bug reports (errors and omissions in the permission map) at:
	http://code.google.com/p/android-permission/issues/list
and we will credit anyone who contributes.

**************************

The permission map is based on our tests of Android 2.2 on a Nexus One, 
although we have added information for other versions and devices.

Of particular note:

--	ACCESS_GPS and ACCESS_LOCATION were deprecated in an early version of
	Android and do not appear in this permission map.  However, they may be
	needed by older applications.

--	We were unable to test WiMax functionality on Samsung or Motorola devices.
	They likely have classes similar to HTC's 
	com.htc.net.wimax.WimaxController.
	
--	Some permissions really do not exist anywhere, such as BRICK.

--	android.os.IMountService exists in Android 2.1 and lower.
	android.os.storage.IMountService replaces it in Android 2.2 and higher.

--	The following are not in this public map because they are deprecated but,
	if you want to know them for use analyzing older applications:
	Delete,content://calendar (API 2.1 and lower),
		android.permission.WRITE_CALENDAR
	Read,content://calendar (API 2.1 and lower),
		android.permission.READ_CALENDAR
	Update,content://calendar (API 2.1 and lower),
		android.permission.WRITE_CALENDAR
	Write,content://calendar (API 2.1 and lower),
		android.permission.WRITE_CALENDAR

*****************************

We would like to thank: 

Royce Cheng-Yue and Kathryn Lingel for their help testing the API and system
Content Providers.