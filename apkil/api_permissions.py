# Copyright 2012, The Honeynet Project. All rights reserved.
# Author: Kun Yang <kelwya@gmail.com>
#
# APKIL is free software: you can redistribute it and/or modify it under 
# the terms of version 3 of the GNU Lesser General Public License as 
# published by the Free Software Foundation.
#
# APKIL is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for 
# more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with APKIL.  If not, see <http://www.gnu.org/licenses/>.

API_BY_PERMISSION = {
"android.permission.BIND_WALLPAPER": {
    "Lcom/android/server/WallpaperManagerService;": [
        "Lcom/android/server/WallpaperManagerService;->bindWallpaperComponentLocked(Landroid/content/ComponentName;)",
    ],
},
"android.permission.FORCE_BACK": {
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->unhandledBack(I)",
    ],
},
"android.permission.READ_CALENDAR": {
    "Landroid/provider/Calendar$Events;": [
        "Landroid/provider/Calendar$Events;->query(Landroid/content/ContentResolver;L[Ljava/lang/String;;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/provider/Calendar$Events;->query(Landroid/content/ContentResolver;L[Ljava/lang/String;;)",
    ],
    "Landroid/provider/Calendar$Calendars;": [
        "Landroid/provider/Calendar$Calendars;->query(Landroid/content/ContentResolver;L[Ljava/lang/String;;Ljava/lang/String;Ljava/lang/String;)",
    ],
    "Landroid/provider/Calendar$CalendarAlerts;": [
        "Landroid/provider/Calendar$CalendarAlerts;->alarmExists(Landroid/content/ContentResolver;JJJ)",
        "Landroid/provider/Calendar$CalendarAlerts;->findNextAlarmTime(Landroid/content/ContentResolver;J)",
        "Landroid/provider/Calendar$CalendarAlerts;->query(Landroid/content/ContentResolver;L[Ljava/lang/String;;Ljava/lang/String;L[Ljava/lang/String;;Ljava/lang/String;)",
    ],
    "Landroid/provider/Calendar$EventDays;": [
        "Landroid/provider/Calendar$EventDays;->query(Landroid/content/ContentResolver;II)",
    ],
    "Landroid/provider/Calendar$Instances;": [
        "Landroid/provider/Calendar$Instances;->query(Landroid/content/ContentResolver;L[Ljava/lang/String;;JJLjava/lang/String;Ljava/lang/String;)",
        "Landroid/provider/Calendar$Instances;->query(Landroid/content/ContentResolver;L[Ljava/lang/String;;JJ)",
    ],
},
"android.permission.READ_SYNC_STATS": {
    "Landroid/app/ContextImpl$ApplicationContentResolver;": [
        "Landroid/app/ContextImpl$ApplicationContentResolver;->getCurrentSync(L;)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->getSyncStatus(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->isSyncActive(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->isSyncPending(Landroid/accounts/Account;Ljava/lang/String;)",
    ],
    "Landroid/content/IContentService$Stub$Proxy;": [
        "Landroid/content/IContentService$Stub$Proxy;->getCurrentSync(L;)",
        "Landroid/content/IContentService$Stub$Proxy;->getSyncStatus(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/IContentService$Stub$Proxy;->isSyncActive(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/IContentService$Stub$Proxy;->isSyncPending(Landroid/accounts/Account;Ljava/lang/String;)",
    ],
    "Landroid/content/ContentService;": [
        "Landroid/content/ContentService;->getCurrentSync(L;)",
        "Landroid/content/ContentService;->getSyncStatus(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/ContentService;->isSyncActive(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/ContentService;->isSyncPending(Landroid/accounts/Account;Ljava/lang/String;)",
    ],
    "Landroid/content/ContentResolver;": [
        "Landroid/content/ContentResolver;->getCurrentSync(L;)",
        "Landroid/content/ContentResolver;->getSyncStatus(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/ContentResolver;->isSyncActive(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/ContentResolver;->isSyncPending(Landroid/accounts/Account;Ljava/lang/String;)",
    ],
},
"android.permission.SHUTDOWN": {
    "Landroid/os/INetworkManagementService$Stub$Proxy;": [
        "Landroid/os/INetworkManagementService$Stub$Proxy;->shutdown(L;)",
    ],
    "Landroid/os/storage/IMountService$Stub$Proxy;": [
        "Landroid/os/storage/IMountService$Stub$Proxy;->shutdown(Landroid/os/storage/IMountShutdownObserver;)",
    ],
    "Landroid/os/IMountService$Stub$Proxy;": [
        "Landroid/os/IMountService$Stub$Proxy;->shutdow(Landroid/os/IMountService$Stub$Proxy/shutdow;)",
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->shutdown(I)",
    ],
},
"android.permission.INTERNET": {
    "Ljava/net/Socket;": [
        "Ljava/net/Socket;-><init>(L;)",
        "Ljava/net/Socket;-><init>(Ljava/lang/String;I)",
        "Ljava/net/Socket;-><init>(Ljava/lang/String;ILjava/net/InetAddress;I)",
        "Ljava/net/Socket;-><init>(Ljava/lang/String;IZ)",
        "Ljava/net/Socket;-><init>(Ljava/net/InetAddress;I)",
        "Ljava/net/Socket;-><init>(Ljava/net/InetAddress;ILjava/net/InetAddress;I)",
        "Ljava/net/Socket;-><init>(Ljava/net/InetAddress;IZ)",
    ],
    "Lorg/apache/http/impl/client/DefaultHttpClient;": [
        "Lorg/apache/http/impl/client/DefaultHttpClient;-><init>(L;)",
        "Lorg/apache/http/impl/client/DefaultHttpClient;-><init>(Lorg/apache/http/params/HttpParams;)",
        "Lorg/apache/http/impl/client/DefaultHttpClient;-><init>(Lorg/apache/http/conn/ClientConnectionManager;Lorg/apache/http/params/HttpParams;)",
        "Lorg/apache/http/impl/client/DefaultHttpClient;->execute(Lorg/apache/http/client/methods/HttpUriRequest;)",
        "Lorg/apache/http/impl/client/DefaultHttpClient;->execute(Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/client/ResponseHandler;Lorg/apache/http/protocol/HttpContext;)",
        "Lorg/apache/http/impl/client/DefaultHttpClient;->execute(Lorg/apache/http/HttpHost;Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/client/ResponseHandler;Lorg/apache/http/protocol/HttpContext;)",
        "Lorg/apache/http/impl/client/DefaultHttpClient;->execute(Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/protocol/HttpContext;)",
        "Lorg/apache/http/impl/client/DefaultHttpClient;->execute(Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/client/ResponseHandler;)",
        "Lorg/apache/http/impl/client/DefaultHttpClient;->execute(Lorg/apache/http/HttpHost;Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/client/ResponseHandler;)",
        "Lorg/apache/http/impl/client/DefaultHttpClient;->execute(Lorg/apache/http/HttpHost;Lorg/apache/http/client/methods/HttpUriRequest;)",
        "Lorg/apache/http/impl/client/DefaultHttpClient;->execute(Lorg/apache/http/HttpHost;Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/protocol/HttpContext;)",
    ],
    "Lcom/android/http/multipart/Part;": [
        "Lcom/android/http/multipart/Part;->send(Ljava/io/OutputStream;)",
        "Lcom/android/http/multipart/Part;->sendParts(Ljava/io/OutputStream;[Lcom/android/http/multipart/Part;)",
        "Lcom/android/http/multipart/Part;->sendParts(Ljava/io/OutputStream;[Lcom/android/http/multipart/Part;[B)",
        "Lcom/android/http/multipart/Part;->sendStart(Ljava/io/OutputStream;)",
        "Lcom/android/http/multipart/Part;->sendTransferEncodingHeader(Ljava/io/OutputStream;)",
    ],
    "Ljava/net/HttpURLConnection;": [
        "Ljava/net/HttpURLConnection;-><init>(Ljava/net/URL;)",
        "Ljava/net/HttpURLConnection;->connect(L;)",
    ],
    "Lorg/apache/http/impl/client/HttpClient;": [
        "Lorg/apache/http/impl/client/HttpClient;->execute(Lorg/apache/http/client/methods/HttpUriRequest;)",
        "Lorg/apache/http/impl/client/HttpClient;->execute(Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/client/ResponseHandler;Lorg/apache/http/protocol/HttpContext;)",
        "Lorg/apache/http/impl/client/HttpClient;->execute(Lorg/apache/http/HttpHost;Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/client/ResponseHandler;Lorg/apache/http/protocol/HttpContext;)",
        "Lorg/apache/http/impl/client/HttpClient;->execute(Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/protocol/HttpContext;)",
        "Lorg/apache/http/impl/client/HttpClient;->execute(Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/client/ResponseHandler;)",
        "Lorg/apache/http/impl/client/HttpClient;->execute(Lorg/apache/http/HttpHost;Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/client/ResponseHandler;)",
        "Lorg/apache/http/impl/client/HttpClient;->execute(Lorg/apache/http/HttpHost;Lorg/apache/http/client/methods/HttpUriRequest;)",
        "Lorg/apache/http/impl/client/HttpClient;->execute(Lorg/apache/http/HttpHost;Lorg/apache/http/client/methods/HttpUriRequest;Lorg/apache/http/protocol/HttpContext;)",
    ],
    "Lcom/android/http/multipart/FilePart;": [
        "Lcom/android/http/multipart/FilePart;->sendData(Ljava/io/OutputStream;)",
        "Lcom/android/http/multipart/FilePart;->sendDispositionHeader(Ljava/io/OutputStream;)",
    ],
    "Ljava/net/URLConnection;": [
        "Ljava/net/URLConnection;->connect(L;)",
        "Ljava/net/URLConnection;->getInputStream(L;)",
    ],
    "Landroid/webkit/WebViewCore;": [
        "Landroid/webkit/WebViewCore;-><init>(Landroid/content/Context;Landroid/webkit/WebView;Landroid/webkit/CallbackProxy;Ljava/util/Map;)",
    ],
    "Ljava/net/URL;": [
        "Ljava/net/URL;->getContent([Ljava/lang/Class;)",
        "Ljava/net/URL;->getContent(L;)",
        "Ljava/net/URL;->openConnection(Ljava/net/Proxy;)",
        "Ljava/net/URL;->openConnection(L;)",
        "Ljava/net/URL;->openStream(L;)",
    ],
    "Ljava/net/ServerSocket;": [
        "Ljava/net/ServerSocket;-><init>(L;)",
        "Ljava/net/ServerSocket;-><init>(I)",
        "Ljava/net/ServerSocket;-><init>(II)",
        "Ljava/net/ServerSocket;-><init>(IILjava/net/InetAddress;)",
        "Ljava/net/ServerSocket;->bind(Ljava/net/SocketAddress;)",
        "Ljava/net/ServerSocket;->bind(Ljava/net/SocketAddress;I)",
    ],
    "Ljava/net/NetworkInterface;": [
        "Ljava/net/NetworkInterface;-><init>(L;)",
        "Ljava/net/NetworkInterface;-><init>(Ljava/lang/String;ILjava/net/InetAddress;)",
    ],
    "Landroid/webkit/WebView;": [
        "Landroid/webkit/WebView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)",
        "Landroid/webkit/WebView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)",
        "Landroid/webkit/WebView;-><init>(Landroid/content/Context;)",
    ],
    "Lcom/android/http/multipart/StringPart;": [
        "Lcom/android/http/multipart/StringPart;->sendData(Ljava/io/OuputStream;)",
    ],
    "Ljava/net/DatagramSocket;": [
        "Ljava/net/DatagramSocket;-><init>(L;)",
        "Ljava/net/DatagramSocket;-><init>(I)",
        "Ljava/net/DatagramSocket;-><init>(ILjava/net/InetAddress;)",
        "Ljava/net/DatagramSocket;-><init>(Ljava/net/SocketAddress;)",
    ],
    "Landroid/app/Activity;": [
        "Landroid/app/Activity;->setContentView(I)",
    ],
    "Landroid/webkit/WebSettings;": [
        "Landroid/webkit/WebSettings;->setBlockNetworkLoads(Z)",
        "Landroid/webkit/WebSettings;->verifyNetworkAccess(L;)",
    ],
    "Ljava/net/MulticastSocket;": [
        "Ljava/net/MulticastSocket;-><init>(L;)",
        "Ljava/net/MulticastSocket;-><init>(I)",
        "Ljava/net/MulticastSocket;-><init>(Ljava/net/SocketAddress;)",
    ],
},
"android.permission.CHANGE_CONFIGURATION": {
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->updateConfiguration(Landroid/content/res/Configuration;)",
    ],
},
"com.android.browser.permission.WRITE_HISTORY_BOOKMARKS": {
    "Landroid/provider/Browser;": [
        "Landroid/provider/Browser;->clearSearches(Landroid/content/ContentResolver;)",
    ],
},
"android.permission.CHANGE_WIFI_MULTICAST_STATE": {
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;": [
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->acquireMulticastLock(Landroid/os/IBinder;Ljava/lang/String;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->initializeMulticastFiltering(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->releaseMulticastLock(L;)",
    ],
    "Landroid/net/wifi/WifiManager$MulticastLock;": [
        "Landroid/net/wifi/WifiManager$MulticastLock;->acquire(L;)",
        "Landroid/net/wifi/WifiManager$MulticastLock;->finalize(L;)",
        "Landroid/net/wifi/WifiManager$MulticastLock;->release(L;)",
    ],
    "Landroid/net/wifi/WifiManager;": [
        "Landroid/net/wifi/WifiManager;->initializeMulticastFiltering(L;)",
    ],
},
"android.permission.SET_TIME_ZONE": {
    "Landroid/app/IAlarmManager$Stub$Proxy;": [
        "Landroid/app/IAlarmManager$Stub$Proxy;->setTimeZone(Ljava/lang/String;)",
    ],
    "Landroid/app/AlarmManager;": [
        "Landroid/app/AlarmManager;->setTimeZone(Ljava/lang/String;)",
    ],
},
"android.permission.WRITE_SYNC_SETTINGS": {
    "Landroid/app/ContextImpl$ApplicationContentResolver;": [
        "Landroid/app/ContextImpl$ApplicationContentResolver;->addPeriodicSync(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;J)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->removePeriodicSync(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->setIsSyncable(Landroid/accounts/Account;Ljava/lang/String;I)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->setMasterSyncAutomatically(Z)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->setSyncAutomatically(Landroid/accounts/Account;Ljava/lang/String;Z)",
    ],
    "Landroid/content/IContentService$Stub$Proxy;": [
        "Landroid/content/IContentService$Stub$Proxy;->addPeriodicSync(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;J)",
        "Landroid/content/IContentService$Stub$Proxy;->removePeriodicSync(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
        "Landroid/content/IContentService$Stub$Proxy;->setIsSyncable(Landroid/accounts/Account;Ljava/lang/String;I)",
        "Landroid/content/IContentService$Stub$Proxy;->setMasterSyncAutomatically(Z)",
        "Landroid/content/IContentService$Stub$Proxy;->setSyncAutomatically(Landroid/accounts/Account;Ljava/lang/String;Z)",
    ],
    "Landroid/content/ContentService;": [
        "Landroid/content/ContentService;->addPeriodicSync(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;J)",
        "Landroid/content/ContentService;->removePeriodicSync(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
        "Landroid/content/ContentService;->setIsSyncable(Landroid/accounts/Account;Ljava/lang/String;I)",
        "Landroid/content/ContentService;->setMasterSyncAutomatically(Z)",
        "Landroid/content/ContentService;->setSyncAutomatically(Landroid/accounts/Account;Ljava/lang/String;Z)",
    ],
    "Landroid/content/ContentResolver;": [
        "Landroid/content/ContentResolver;->addPeriodicSync(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;J)",
        "Landroid/content/ContentResolver;->removePeriodicSync(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
        "Landroid/content/ContentResolver;->setIsSyncable(Landroid/accounts/Account;Ljava/lang/String;I)",
        "Landroid/content/ContentResolver;->setMasterSyncAutomatically(Z)",
        "Landroid/content/ContentResolver;->setSyncAutomatically(Landroid/accounts/Account;Ljava/lang/String;Z)",
    ],
},
"android.permission.CHANGE_WIMAX_STATE": {
    "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;": [
        "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;->setWimaxEnable(Lcom/htc/net/wimax/WimaxController$Stub$Proxy/setWimaxEnable;)",
    ],
},
"android.permission.READ_LOGS": {
    "Lcom/android/internal/os/IDropBoxManagerService$Stub$Proxy;": [
        "Lcom/android/internal/os/IDropBoxManagerService$Stub$Proxy;->getNextEntry(Ljava/lang/String;J)",
    ],
    "Ljava/lang/Runtime;": [
        "Ljava/lang/Runtime;->exec(Ljava/lang/String;)",
        "Ljava/lang/Runtime;->exec([Ljava/lang/String;)",
        "Ljava/lang/Runtime;->exec([Ljava/lang/String;[Ljava/lang/String;)",
        "Ljava/lang/Runtime;->exec([Ljava/lang/String;[Ljava/lang/String;Ljava/io/File;)",
        "Ljava/lang/Runtime;->exec(Ljava/lang/String;[Ljava/lang/String;)",
        "Ljava/lang/Runtime;->exec(Ljava/lang/String;[Ljava/lang/String;Ljava/io/File;)",
    ],
    "Landroid/os/DropBoxManager;": [
        "Landroid/os/DropBoxManager;->getNextEntry(Ljava/lang/String;J)",
    ],
},
"android.permission.INJECT_EVENTS": {
    "Landroid/view/IWindowManager$Stub$Proxy;": [
        "Landroid/view/IWindowManager$Stub$Proxy;->injectKeyEvent(Landroid/view/KeyEvent;Z)",
        "Landroid/view/IWindowManager$Stub$Proxy;->injectPointerEvent(Landroid/view/MotionEvent;Z)",
        "Landroid/view/IWindowManager$Stub$Proxy;->injectTrackballEvent(Landroid/view/MotionEvent;Z)",
    ],
    "Landroid/app/Instrumentation;": [
        "Landroid/app/Instrumentation;->invokeContextMenuAction(Landroid/app/Activity;II)",
        "Landroid/app/Instrumentation;->sendCharacterSync(I)",
        "Landroid/app/Instrumentation;->sendKeyDownUpSync(I)",
        "Landroid/app/Instrumentation;->sendKeySync(Landroid/view/KeyEvent;)",
        "Landroid/app/Instrumentation;->sendPointerSync(Landroid/view/MotionEvent;)",
        "Landroid/app/Instrumentation;->sendStringSync(Ljava/lang/String;)",
        "Landroid/app/Instrumentation;->sendTrackballEventSync(Landroid/view/MotionEvent;)",
    ],
},
"android.permission.BIND_DEVICE_ADMIN": {
    "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;": [
        "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;->getRemoveWarning(Landroid/content/ComponentName;Landroid/os/RemoteCallback;)",
        "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;->reportFailedPasswordAttempt(L;)",
        "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;->reportSuccessfulPasswordAttempt(L;)",
        "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;->setActiveAdmin(Landroid/content/ComponentName;)",
        "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;->setActivePasswordState(II)",
    ],
    "Landroid/app/admin/DevicePolicyManager;": [
        "Landroid/app/admin/DevicePolicyManager;->getRemoveWarning(Landroid/content/ComponentName;Landroid/os/RemoteCallback;)",
        "Landroid/app/admin/DevicePolicyManager;->reportFailedPasswordAttempt(L;)",
        "Landroid/app/admin/DevicePolicyManager;->reportSuccessfulPasswordAttempt(L;)",
        "Landroid/app/admin/DevicePolicyManager;->setActiveAdmin(Landroid/content/ComponentName;)",
        "Landroid/app/admin/DevicePolicyManager;->setActivePasswordState(II)",
    ],
},
"android.permission.FORCE_STOP_PACKAGES": {
    "Landroid/app/ActivityManager;": [
        "Landroid/app/ActivityManager;->forceStopPackage(Ljava/lang/String;)",
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->forceStopPackage(Ljava/lang/String;)",
    ],
    "Landroid/app/ActivityManagerNative;": [
        "Landroid/app/ActivityManagerNative;->forceStopPackage(Ljava/lang/String;)",
    ],
},
"android.permission.WRITE_SECURE_SETTINGS": {
    "Landroid/os/IPowerManager$Stub$Proxy;": [
        "Landroid/os/IPowerManager$Stub$Proxy;->setMaximumScreenOffTimeount(I)",
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->setInstallLocation(I)",
    ],
    "Landroid/server/BluetoothService;": [
        "Landroid/server/BluetoothService;->setScanMode(II)",
    ],
    "Landroid/bluetooth/BluetoothAdapter;": [
        "Landroid/bluetooth/BluetoothAdapter;->setScanMode(II)",
        "Landroid/bluetooth/BluetoothAdapter;->setScanMode(I)",
    ],
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;": [
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->setScanMode(II)",
    ],
},
"android.permission.UPDATE_DEVICE_STATS": {
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;": [
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteFullWifiLockAcquired(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteFullWifiLockReleased(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteInputEvent(L;)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->notePhoneDataConnectionState(IZ)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->notePhoneOff(L;)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->notePhoneOn(L;)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->notePhoneSignalStrength(LSignalStrength;)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->notePhoneState(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteScanWifiLockAcquired(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteScanWifiLockReleased(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteScreenBrightness(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteScreenOff(L;)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteScreenOn(L;)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteStartGps(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteStartSensor(II)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteStartWakelock(ILjava/lang/String;I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteStopGps(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteStopSensor(II)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteStopWakelock(ILjava/lang/String;I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteUserActivity(II)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteWifiMulticastDisabled(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteWifiMulticastEnabled(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteWifiOff(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteWifiOn(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteWifiRunning(L;)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->noteWifiStopped(L;)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->recordCurrentLevel(I)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->setOnBattery(ZI)",
    ],
    "Lcom/android/internal/app/IUsageStats$Stub$Proxy;": [
        "Lcom/android/internal/app/IUsageStats$Stub$Proxy;->notePauseComponent(LComponentName;)",
        "Lcom/android/internal/app/IUsageStats$Stub$Proxy;->noteResumeComponent(LComponentName;)",
    ],
},
"android.permission.ACCESS_DRM": {
    "Landroid/provider/DrmStore;": [
        "Landroid/provider/DrmStore;->enforceAccessDrmPermission(Landroid/content/Context;)",
    ],
},
"android.permission.SYSTEM_ALERT_WINDOW": {
    "Landroid/view/IWindowSession$Stub$Proxy;": [
        "Landroid/view/IWindowSession$Stub$Proxy;->add(Landroid/view/IWindow;Landroid/view/WindowManager$LayoutParams;ILandroid/graphics/Rect;)",
    ],
},
"android.permission.DUMP": {
    "Landroid/view/IWindowManager$Stub$Proxy;": [
        "Landroid/view/IWindowManager$Stub$Proxy;->isViewServerRunning(L;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->startViewServer(I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->stopViewServer(L;)",
    ],
    "Landroid/content/ContentService;": [
        "Landroid/content/ContentService;->dump(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;L[Ljava/lang/String;;)",
    ],
    "Lcom/android/server/WallpaperManagerService;": [
        "Lcom/android/server/WallpaperManagerService;->dump(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;L[Ljava/lang/String;)",
    ],
},
"android.permission.CHANGE_WIFI_STATE": {
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;": [
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->addOrUpdateNetwork(Landroid/net/wifi/WifiConfiguration;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->disableNetwork(I)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->disconnect(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->enableNetwork(IZ)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->pingSupplicant(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->reassociate(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->reconnect(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->removeNetwork(I)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->saveConfiguration(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->setNumAllowedChannels(IZ)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->setWifiApEnabled(Landroid/net/wifi/WifiConfiguration;Z)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->setWifiEnabled(Z)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->startScan(Z)",
    ],
    "Landroid/net/wifi/WifiManager;": [
        "Landroid/net/wifi/WifiManager;->addNetwork(Landroid/net/wifi/WifiConfiguration;)",
        "Landroid/net/wifi/WifiManager;->addOrUpdateNetwork(Landroid/net/wifi/WifiConfiguration;)",
        "Landroid/net/wifi/WifiManager;->disableNetwork(I)",
        "Landroid/net/wifi/WifiManager;->disconnect(L;)",
        "Landroid/net/wifi/WifiManager;->enableNetwork(IZ)",
        "Landroid/net/wifi/WifiManager;->pingSupplicant(L;)",
        "Landroid/net/wifi/WifiManager;->reassociate(L;)",
        "Landroid/net/wifi/WifiManager;->reconnect(L;)",
        "Landroid/net/wifi/WifiManager;->removeNetwork(I)",
        "Landroid/net/wifi/WifiManager;->saveConfiguration(L;)",
        "Landroid/net/wifi/WifiManager;->setNumAllowedChannels(IZ)",
        "Landroid/net/wifi/WifiManager;->setWifiApEnabled(Landroid/net/wifi/WifiConfiguration;Z)",
        "Landroid/net/wifi/WifiManager;->setWifiEnabled(Z)",
        "Landroid/net/wifi/WifiManager;->startScan(L;)",
        "Landroid/net/wifi/WifiManager;->startScanActive(L;)",
    ],
},
"android.permission.RECORD_AUDIO": {
    "Landroid/media/AudioRecord;": [
        "Landroid/media/AudioRecord;-><init>(IIIII)",
    ],
    "Landroid/media/MediaRecorder;": [
        "Landroid/media/MediaRecorder;->setAudioSource(I)",
    ],
    "Landroid/speech/SpeechRecognizer;": [
        "Landroid/speech/SpeechRecognizer;->cancel(L;)",
        "Landroid/speech/SpeechRecognizer;->handleCancelMessage(L;)",
        "Landroid/speech/SpeechRecognizer;->handleStartListening(Landroid/content/Intent;)",
        "Landroid/speech/SpeechRecognizer;->handleStopMessage(L;)",
        "Landroid/speech/SpeechRecognizer;->startListening(Landroid/content/Intent;)",
        "Landroid/speech/SpeechRecognizer;->stopListening(L;)",
    ],
},
"android.permission.MODIFY_PHONE_STATE": {
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;": [
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;->notifyCallForwardingChanged(Z)",
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;->notifyCallState(ILjava/lang/String;)",
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;->notifyCellLocation(Landroid/os/Bundle;)",
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;->notifyDataActivity(I)",
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;->notifyDataConnection(IZLjava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;I)",
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;->notifyDataConnectionFailed(Ljava/lang/String;)",
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;->notifyMessageWaitingChanged(Z)",
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;->notifyServiceState(Landroid/telephony/ServiceState;)",
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;->notifySignalStrength(Landroid/telephony/SignalStrength;)",
    ],
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;": [
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->answerRingingCall(L;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->cancelMissedCallsNotification(L;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->disableApnType(Ljava/lang/String;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->disableDataConnectivity(L;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->enableApnType(Ljava/lang/String;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->enableDataConnectivity(L;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->handlePinMmi(Ljava/lang/String;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->setRadio(Z)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->silenceRinger(L;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->supplyPin(Ljava/lang/String;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->toggleRadioOnOff(L;)",
    ],
    "Landroid/net/MobileDataStateTracker;": [
        "Landroid/net/MobileDataStateTracker;->reconnect(L;)",
        "Landroid/net/MobileDataStateTracker;->setRadio(Z)",
        "Landroid/net/MobileDataStateTracker;->teardown(L;)",
    ],
},
"android.permission.ACCOUNT_MANAGER": {
    "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;": [
        "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;->addAccount(Landroid/accounts/IAccountAuthenticatorResponse;Ljava/lang/String;Ljava/lang/String;L[Ljava/lang/String;;Landroid/os/Bundle;)",
        "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;->confirmCredentials(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;Landroid/os/Bundle;)",
        "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;->editProperties(Landroid/accounts/IAccountAuthenticatorResponse;Ljava/lang/String;)",
        "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;->getAccountRemovalAllowed(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;)",
        "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;->getAuthToken(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
        "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;->getAuthTokenLabel(Landroid/accounts/IAccountAuthenticatorResponse;Ljava/lang/String;)",
        "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;->hasFeatures(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;L[Ljava/lang/String;;)",
        "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;->updateCredentials(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/accounts/AbstractAccountAuthenticator;": [
        "Landroid/accounts/AbstractAccountAuthenticator;->checkBinderPermission(L;)",
        "Landroid/accounts/AbstractAccountAuthenticator;->confirmCredentials(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;Landroid/os/Bundle;)",
        "Landroid/accounts/AbstractAccountAuthenticator;->editProperties(Landroid/accounts/IAccountAuthenticatorResponse;Ljava/lang/String;)",
        "Landroid/accounts/AbstractAccountAuthenticator;->getAccountRemovalAllowed(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;)",
        "Landroid/accounts/AbstractAccountAuthenticator;->getAuthToken(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
        "Landroid/accounts/AbstractAccountAuthenticator;->getAuthTokenLabel(Landroid/accounts/IAccountAuthenticatorResponse;Ljava/lang/String;)",
        "Landroid/accounts/AbstractAccountAuthenticator;->hasFeatures(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;L[Ljava/lang/String;;)",
        "Landroid/accounts/AbstractAccountAuthenticator;->updateCredentials(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
        "Landroid/accounts/AbstractAccountAuthenticator;->addAccount(Landroid/accounts/IAccountAuthenticatorResponse;Ljava/lang/String;Ljava/lang/String;L[Ljava/lang/String;;Landroid/os/Bundle;)",
    ],
    "Landroid/accounts/AbstractAccountAuthenticator$Transport;": [
        "Landroid/accounts/AbstractAccountAuthenticator$Transport;->addAccount(Landroid/accounts/IAccountAuthenticatorResponse;Ljava/lang/String;Ljava/lang/String;L[Ljava/lang/String;;Landroid/os/Bundle;)",
        "Landroid/accounts/AbstractAccountAuthenticator$Transport;->confirmCredentials(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;Landroid/os/Bundle;)",
        "Landroid/accounts/AbstractAccountAuthenticator$Transport;->editProperties(Landroid/accounts/IAccountAuthenticatorResponse;Ljava/lang/String;)",
        "Landroid/accounts/AbstractAccountAuthenticator$Transport;->getAccountRemovalAllowed(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;)",
        "Landroid/accounts/AbstractAccountAuthenticator$Transport;->getAuthToken(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
        "Landroid/accounts/AbstractAccountAuthenticator$Transport;->getAuthTokenLabel(Landroid/accounts/IAccountAuthenticatorResponse;Ljava/lang/String;)",
        "Landroid/accounts/AbstractAccountAuthenticator$Transport;->hasFeatures(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;L[Ljava/lang/String;;)",
        "Landroid/accounts/AbstractAccountAuthenticator$Transport;->updateCredentials(Landroid/accounts/IAccountAuthenticatorResponse;Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
    ],
},
"android.permission.SET_ANIMATION_SCALE": {
    "Landroid/view/IWindowManager$Stub$Proxy;": [
        "Landroid/view/IWindowManager$Stub$Proxy;->setAnimationScale(IF)",
        "Landroid/view/IWindowManager$Stub$Proxy;->setAnimationScales(L[F;)",
    ],
},
"android.permission.SET_PROCESS_LIMIT": {
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->setProcessForeground(Landroid/os/IBinder;IZ)",
        "Landroid/app/IActivityManager$Stub$Proxy;->setProcessLimit(I)",
    ],
},
"android.permission.MOVE_PACKAGE": {
    "Landroid/app/ContextImpl$ApplicationPackageManager;": [
        "Landroid/app/ContextImpl$ApplicationPackageManager;->movePackage(LString;LIPackageMoveObserver;I)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->movePackage(Ljava/lang/String;LIPackageMoveObserver;I)",
    ],
    "Landroid/content/pm/PackageManager;": [
        "Landroid/content/pm/PackageManager;->movePackage(Ljava/lang/String;LIPackageMoveObserver;I)",
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->movePackage(Ljava/lang/String;Landroid/content/pm/IPackageMoveObserver;I)",
    ],
},
"android.permission.SET_DEBUG_APP": {
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->setDebugApp(Ljava/lang/String;ZZ)",
    ],
},
"Only": {
    "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->updateExternalMediaStatus(ZZ)",
    ],
},
"android.permission.BLUETOOTH": {
    "Landroid/bluetooth/BluetoothSocket;": [
        "Landroid/bluetooth/BluetoothSocket;->connect(L;)",
    ],
    "Landroid/server/BluetoothService;": [
        "Landroid/server/BluetoothService;->addRemoteDeviceProperties(Ljava/lang/String;L[Ljava/lang/String;;)",
        "Landroid/server/BluetoothService;->addRfcommServiceRecord(Ljava/lang/String;Landroid/os/ParcelUuid;ILandroid/os/IBinder;)",
        "Landroid/server/BluetoothService;->fetchRemoteUuids(Ljava/lang/String;Landroid/os/ParcelUuid;Landroid/bluetooth/IBluetoothCallback;)",
        "Landroid/server/BluetoothService;->getAddress(L;)",
        "Landroid/server/BluetoothService;->getAddressFromObjectPath(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->getAllProperties(L;)",
        "Landroid/server/BluetoothService;->getBluetoothState(L;)",
        "Landroid/server/BluetoothService;->getBondState(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->getDiscoverableTimeout(L;)",
        "Landroid/server/BluetoothService;->getName(L;)",
        "Landroid/server/BluetoothService;->getObjectPathFromAddress(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->getProperty(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->getPropertyInternal(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->getRemoteClass(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->getRemoteName(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->getRemoteServiceChannel(Ljava/lang/String;Landroid/os/ParcelUuid;)",
        "Landroid/server/BluetoothService;->getRemoteUuids(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->getScanMode(L;)",
        "Landroid/server/BluetoothService;->getTrustState(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->isDiscovering(L;)",
        "Landroid/server/BluetoothService;->isEnabled(L;)",
        "Landroid/server/BluetoothService;->listBonds(L;)",
        "Landroid/server/BluetoothService;->removeServiceRecord(I)",
        "Landroid/server/BluetoothService;->sendUuidIntent(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->setLinkTimeout(Ljava/lang/String;I)",
        "Landroid/server/BluetoothService;->setPropertyBoolean(Ljava/lang/String;Z)",
        "Landroid/server/BluetoothService;->setPropertyInteger(Ljava/lang/String;I)",
        "Landroid/server/BluetoothService;->setPropertyString(Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->updateDeviceServiceChannelCache(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->updateRemoteDevicePropertiesCache(Ljava/lang/String;)",
    ],
    "Landroid/bluetooth/BluetoothPbap;": [
        "Landroid/bluetooth/BluetoothPbap;->getClient(L;)",
        "Landroid/bluetooth/BluetoothPbap;->getState(L;)",
        "Landroid/bluetooth/BluetoothPbap;->isConnected(Landroid/bluetooth/BluetoothDevice;)",
    ],
    "Landroid/bluetooth/BluetoothHeadset;": [
        "Landroid/bluetooth/BluetoothHeadset;->getBatteryUsageHint(L;)",
        "Landroid/bluetooth/BluetoothHeadset;->getCurrentHeadset(L;)",
        "Landroid/bluetooth/BluetoothHeadset;->getPriority(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/BluetoothHeadset;->getState(L;)",
        "Landroid/bluetooth/BluetoothHeadset;->isConnected(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/BluetoothHeadset;->startVoiceRecognition(L;)",
        "Landroid/bluetooth/BluetoothHeadset;->stopVoiceRecognition(L;)",
    ],
    "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;": [
        "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;->getClient(L;)",
        "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;->getState(L;)",
        "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;->isConnected(Landroid/bluetooth/BluetoothDevice;)",
    ],
    "Landroid/bluetooth/BluetoothAdapter;": [
        "Landroid/bluetooth/BluetoothAdapter;->getAddress(L;)",
        "Landroid/bluetooth/BluetoothAdapter;->getBondedDevices(L;)",
        "Landroid/bluetooth/BluetoothAdapter;->getDiscoverableTimeout(L;)",
        "Landroid/bluetooth/BluetoothAdapter;->getName(L;)",
        "Landroid/bluetooth/BluetoothAdapter;->getScanMode(L;)",
        "Landroid/bluetooth/BluetoothAdapter;->getState(L;)",
        "Landroid/bluetooth/BluetoothAdapter;->isDiscovering(L;)",
        "Landroid/bluetooth/BluetoothAdapter;->isEnabled(L;)",
        "Landroid/bluetooth/BluetoothAdapter;->listenUsingRfcommWithServiceRecord(Ljava/lang/String;Ljava/util/UUID;)",
    ],
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;": [
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->addRfcommServiceRecord(Ljava/lang/String;Landroid/os/ParcelUuid;ILandroid/os/IBinder;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->fetchRemoteUuids(Ljava/lang/String;Landroid/os/ParcelUuid;Landroid/bluetooth/IBluetoothCallback;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->getAddress(L;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->getBluetoothState(L;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->getBondState(Ljava/lang/String;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->getDiscoverableTimeout(L;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->getName(L;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->getRemoteClass(Ljava/lang/String;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->getRemoteName(Ljava/lang/String;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->getRemoteServiceChannel(Ljava/lang/String;Landroid/os/ParcelUuid;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->getRemoteUuids(Ljava/lang/String;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->getScanMode(L;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->getTrustState(Ljava/lang/String;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->isDiscovering(L;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->isEnabled(L;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->listBonds(L;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->removeServiceRecord(I)",
    ],
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;": [
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;->getBatteryUsageHint(L;)",
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;->getCurrentHeadset(L;)",
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;->getPriority(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;->getState(L;)",
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;->isConnected(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;->startVoiceRecognition(L;)",
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;->stopVoiceRecognition(L;)",
    ],
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;": [
        "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;->getConnectedSinks(L;)",
        "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;->getNonDisconnectedSinks(L;)",
        "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;->getSinkPriority(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;->getSinkState(Landroid/bluetooth/BluetoothDevice;)",
    ],
    "Landroid/bluetooth/BluetoothDevice;": [
        "Landroid/bluetooth/BluetoothDevice;->createRfcommSocketToServiceRecord(Ljava/util/UUID;)",
        "Landroid/bluetooth/BluetoothDevice;->fetchUuidsWithSdp(L;)",
        "Landroid/bluetooth/BluetoothDevice;->getBondState(L;)",
        "Landroid/bluetooth/BluetoothDevice;->getName(L;)",
        "Landroid/bluetooth/BluetoothDevice;->getServiceChannel(Landroid/os/ParcelUuid;)",
        "Landroid/bluetooth/BluetoothDevice;->getUuids(L;)",
    ],
    "Landroid/bluetooth/BluetoothA2dp;": [
        "Landroid/bluetooth/BluetoothA2dp;->getConnectedSinks(L;)",
        "Landroid/bluetooth/BluetoothA2dp;->getNonDisconnectedSinks(L;)",
        "Landroid/bluetooth/BluetoothA2dp;->getSinkPriority(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/BluetoothA2dp;->getSinkState(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/BluetoothA2dp;->isSinkConnected(Landroid/bluetooth/BluetoothDevice;)",
    ],
    "Landroid/server/BluetoothA2dpService;": [
        "Landroid/server/BluetoothA2dpService;-><init>(Landroid/content/Context;Landroid/server/BluetoothService;)",
        "Landroid/server/BluetoothA2dpService;->addAudioSink(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/server/BluetoothA2dpService;->getConnectedSinks(L;)",
        "Landroid/server/BluetoothA2dpService;->getNonDisconnectedSinks(L;)",
        "Landroid/server/BluetoothA2dpService;->getSinkPriority(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/server/BluetoothA2dpService;->getSinkState(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/server/BluetoothA2dpService;->isSinkDevice(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/server/BluetoothA2dpService;->lookupSinksMatchingStates([I)",
        "Landroid/server/BluetoothA2dpService;->onConnectSinkResult(Ljava/lang/String;Z)",
        "Landroid/server/BluetoothA2dpService;->onSinkPropertyChanged(Ljava/lang/String;L[Ljava/lang/String;;)",
    ],
},
"android.permission.CAMERA": {
    "Landroid/hardware/Camera;": [
        "Landroid/hardware/Camera;->native_setup(Ljava/lang/Object;)",
        "Landroid/hardware/Camera;->open(L;)",
    ],
    "Landroid/media/MediaRecorder;": [
        "Landroid/media/MediaRecorder;->setVideoSource(I)",
    ],
},
"android.permission.SET_WALLPAPER_HINTS": {
    "Landroid/app/WallpaperManager;": [
        "Landroid/app/WallpaperManager;->suggestDesiredDimensions(II)",
    ],
    "Landroid/app/IWallpaperManager$Stub$Proxy;": [
        "Landroid/app/IWallpaperManager$Stub$Proxy;->setDimensionHints(II)",
    ],
},
"android.permission.CONTROL_LOCATION_UPDATES": {
    "Landroid/telephony/TelephonyManager;": [
        "Landroid/telephony/TelephonyManager;->disableLocationUpdates(L;)",
        "Landroid/telephony/TelephonyManager;->enableLocationUpdates(L;)",
    ],
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;": [
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->disableLocationUpdates(L;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->enableLocationUpdates(L;)",
    ],
},
"android.permission.REBOOT": {
    "Landroid/os/IPowerManager$Stub$Proxy;": [
        "Landroid/os/IPowerManager$Stub$Proxy;->crash(Ljava/lang/String;)",
        "Landroid/os/IPowerManager$Stub$Proxy;->reboot(Ljava/lang/String;)",
    ],
    "Landroid/os/PowerManager;": [
        "Landroid/os/PowerManager;->reboot(Ljava/lang/String;)",
    ],
    "Landroid/os/RecoverySystem;": [
        "Landroid/os/RecoverySystem;->bootCommand(Landroid/content/Context;Ljava/lang/String;)",
        "Landroid/os/RecoverySystem;->installPackage(Landroid/content/Context;Ljava/io/File;)",
        "Landroid/os/RecoverySystem;->rebootWipeUserData(Landroid/content/Context;)",
    ],
},
"android.permission.SET_WALLPAPER_COMPONENT": {
    "Landroid/app/IWallpaperManager$Stub$Proxy;": [
        "Landroid/app/IWallpaperManager$Stub$Proxy;->setWallpaperComponent(Landroid/content/ComponentName;)",
    ],
},
"android.permission.ACCESS_NETWORK_STATE": {
    "Landroid/net/ConnectivityManager;": [
        "Landroid/net/ConnectivityManager;->getActiveNetworkInfo(L;)",
        "Landroid/net/ConnectivityManager;->getAllNetworkInfo(L;)",
        "Landroid/net/ConnectivityManager;->getLastTetherError(Ljava/lang/String;)",
        "Landroid/net/ConnectivityManager;->getMobileDataEnabled(L;)",
        "Landroid/net/ConnectivityManager;->getNetworkInfo(I)",
        "Landroid/net/ConnectivityManager;->getNetworkPreference(L;)",
        "Landroid/net/ConnectivityManager;->getTetherableIfaces(L;)",
        "Landroid/net/ConnectivityManager;->getTetherableUsbRegexs(L;)",
        "Landroid/net/ConnectivityManager;->getTetherableWifiRegexs(L;)",
        "Landroid/net/ConnectivityManager;->getTetheredIfaces(L;)",
        "Landroid/net/ConnectivityManager;->getTetheringErroredIfaces(L;)",
        "Landroid/net/ConnectivityManager;->isTetheringSupported(L;)",
    ],
    "Landroid/net/IConnectivityManager$Stub$Proxy;": [
        "Landroid/net/IConnectivityManager$Stub$Proxy;->getActiveNetworkInfo(L;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->getAllNetworkInfo(L;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->getLastTetherError(Ljava/lang/String;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->getMobileDataEnabled(L;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->getNetworkInfo(I)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->getNetworkPreference(L;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->getTetherableIfaces(L;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->getTetherableUsbRegexs(L;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->getTetherableWifiRegexs(L;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->getTetheredIfaces(L;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->getTetheringErroredIfaces(L;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->isTetheringSupported(L;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->startUsingNetworkFeature(ILjava/lang/String;Landroid/os/IBinder;)",
    ],
    "Landroid/net/http/RequestQueue;": [
        "Landroid/net/http/RequestQueue;->enablePlatformNotifications(L;)",
        "Landroid/net/http/RequestQueue;->setProxyConfig(L;)",
    ],
    "Landroid/net/ThrottleManager;": [
        "Landroid/net/ThrottleManager;->getByteCount(Ljava/lang/String;III)",
        "Landroid/net/ThrottleManager;->getCliffLevel(Ljava/lang/String;I)",
        "Landroid/net/ThrottleManager;->getCliffThreshold(Ljava/lang/String;I)",
        "Landroid/net/ThrottleManager;->getHelpUri(L;)",
        "Landroid/net/ThrottleManager;->getPeriodStartTime(Ljava/lang/String;)",
        "Landroid/net/ThrottleManager;->getResetTime(Ljava/lang/String;)",
    ],
    "Landroid/net/IThrottleManager$Stub$Proxy;": [
        "Landroid/net/IThrottleManager$Stub$Proxy;->getByteCount(Ljava/lang/String;III)",
        "Landroid/net/IThrottleManager$Stub$Proxy;->getCliffLevel(Ljava/lang/String;I)",
        "Landroid/net/IThrottleManager$Stub$Proxy;->getCliffThreshold(Ljava/lang/String;I)",
        "Landroid/net/IThrottleManager$Stub$Proxy;->getHelpUri(L;)",
        "Landroid/net/IThrottleManager$Stub$Proxy;->getPeriodStartTime(Ljava/lang/String;)",
        "Landroid/net/IThrottleManager$Stub$Proxy;->getResetTime(Ljava/lang/String;)",
        "Landroid/net/IThrottleManager$Stub$Proxy;->getThrottle(Ljava/lang/String;)",
    ],
    "Landroid/net/NetworkInfo;": [
        "Landroid/net/NetworkInfo;->isConnectedOrConnecting(L;)",
    ],
    "Landroid/os/INetworkManagementService$Stub$Proxy;": [
        "Landroid/os/INetworkManagementService$Stub$Proxy;->getDnsForwarders(L;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->getInterfaceRxCounter(Ljava/lang/String;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->getInterfaceRxThrottle(Ljava/lang/String;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->getInterfaceTxCounter(Ljava/lang/String;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->getInterfaceTxThrottle(Ljava/lang/String;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->getIpForwardingEnabled(L;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->isTetheringStarted(L;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->isUsbRNDISStarted(L;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->listInterfaces(L;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->listTetheredInterfaces(L;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->listTtys(L;)",
    ],
},
"android.permission.STATUS_BAR": {
    "Landroid/app/IStatusBar$Stub$Proxy;": [
        "Landroid/app/IStatusBar$Stub$Proxy;->addIcon(Ljava/lang/String;Ljava/lang/String;II)",
        "Landroid/app/IStatusBar$Stub$Proxy;->disable(ILandroid/os/IBinder;Ljava/lang/String;)",
        "Landroid/app/IStatusBar$Stub$Proxy;->removeIcon(Landroid/os/IBinder;)",
        "Landroid/app/IStatusBar$Stub$Proxy;->updateIcon(Landroid/os/IBinder;Ljava/lang/String;Ljava/lang/String;II)",
    ],
    "Landroid/app/StatusBarManager;": [
        "Landroid/app/StatusBarManager;->addIcon(Ljava/lang/String;II)",
        "Landroid/app/StatusBarManager;->disable(I)",
        "Landroid/app/StatusBarManager;->removeIcon(Landroid/os/IBinder;)",
        "Landroid/app/StatusBarManager;->updateIcon(Landroid/os/IBinder;Ljava/lang/String;II)",
    ],
},
"android.permission.WRITE_USER_DICTIONARY": {
    "Landroid/provider/UserDictionary$Words;": [
        "Landroid/provider/UserDictionary$Words;->addWord(Landroid/content/Context;Ljava/lang/String;II)",
    ],
},
"com.android.browser.permission.READ_HISTORY_BOOKMARKS": {
    "Landroid/webkit/WebIconDatabase;": [
        "Landroid/webkit/WebIconDatabase;->bulkRequestIconForPageUrl(Landroid/content/ContentResolver;Ljava/lang/String;Landroid/webkit/WebIconDatabase$IconListener;)",
    ],
    "Landroid/provider/Browser;": [
        "Landroid/provider/Browser;->addSearchUrl(Landroid/content/ContentResolver;Ljava/lang/String;)",
        "Landroid/provider/Browser;->canClearHistory(Landroid/content/ContentResolver;)",
        "Landroid/provider/Browser;->clearHistory(Landroid/content/ContentResolver;)",
        "Landroid/provider/Browser;->deleteFromHistory(Landroid/content/ContentResolver;Ljava/lang/String;)",
        "Landroid/provider/Browser;->deleteHistoryTimeFrame(Landroid/content/ContentResolver;JJ)",
        "Landroid/provider/Browser;->deleteHistoryWhere(Landroid/content/ContentResolver;Ljava/lang/String;)",
        "Landroid/provider/Browser;->getAllBookmarks(Landroid/content/ContentResolver;)",
        "Landroid/provider/Browser;->getAllVisitedUrls(Landroid/content/ContentResolver;)",
        "Landroid/provider/Browser;->getVisitedHistory(Landroid/content/ContentResolver;)",
        "Landroid/provider/Browser;->getVisitedLike(Landroid/content/ContentResolver;Ljava/lang/String;)",
        "Landroid/provider/Browser;->requestAllIcons(Landroid/content/ContentResolver;Ljava/lang/String;Landroid/webkit/WebIconDatabase$IconListener;)",
        "Landroid/provider/Browser;->truncateHistory(Landroid/content/ContentResolver;)",
        "Landroid/provider/Browser;->updateVisitedHistory(Landroid/content/ContentResolver;Ljava/lang/String;Z)",
    ],
},
"android.permission.MOUNT_FORMAT_FILESYSTEMS": {
    "Landroid/os/storage/IMountService$Stub$Proxy;": [
        "Landroid/os/storage/IMountService$Stub$Proxy;->formatVolume(Ljava/lang/String;)",
    ],
    "Landroid/os/IMountService$Stub$Proxy;": [
        "Landroid/os/IMountService$Stub$Proxy;->formatMedi(Landroid/os/IMountService$Stub$Proxy/formatMedi;)",
    ],
},
"android.permission.RECEIVE_SMS": {
    "Landroid/telephony/SmsManager;": [
        "Landroid/telephony/SmsManager;->copyMessageToIcc(L[B;L[B;I)",
        "Landroid/telephony/SmsManager;->deleteMessageFromIcc(I)",
        "Landroid/telephony/SmsManager;->getAllMessagesFromIcc(L;)",
        "Landroid/telephony/SmsManager;->updateMessageOnIcc(IIL[B;)",
    ],
    "Lcom/android/internal/telephony/ISms$Stub$Proxy;": [
        "Lcom/android/internal/telephony/ISms$Stub$Proxy;->copyMessageToIccEf(I[B[B)",
        "Lcom/android/internal/telephony/ISms$Stub$Proxy;->getAllMessagesFromIccEf(L;)",
        "Lcom/android/internal/telephony/ISms$Stub$Proxy;->updateMessageOnIccEf(II[B)",
    ],
    "Landroid/telephony/gsm/SmsManager;": [
        "Landroid/telephony/gsm/SmsManager;->copyMessageToSim(L[B;L[B;I)",
        "Landroid/telephony/gsm/SmsManager;->deleteMessageFromSim(I)",
        "Landroid/telephony/gsm/SmsManager;->getAllMessagesFromSim(L;)",
        "Landroid/telephony/gsm/SmsManager;->updateMessageOnSim(IIL[B;)",
    ],
},
"android.permission.WRITE_CONTACTS": {
    "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;": [
        "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;->updateAdnRecordsInEfByIndex(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)",
        "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;->updateAdnRecordsInEfBySearch(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)",
    ],
    "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;": [
        "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;->updateAdnRecordsInEfByIndex(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;)",
        "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;->updateAdnRecordsInEfBySearch(ILjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)",
    ],
    "Landroid/pim/vcard/VCardEntryCommitter;": [
        "Landroid/pim/vcard/VCardEntryCommitter;->onEntryCreated(Landroid/pim/vcard/VCardEntry;)",
    ],
    "Landroid/pim/vcard/VCardEntry;": [
        "Landroid/pim/vcard/VCardEntry;->pushIntoContentResolver(Landroid/content/ContentResolver;)",
    ],
    "Landroid/provider/Contacts$Settings;": [
        "Landroid/provider/Contacts$Settings;->setSetting(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)",
    ],
    "Landroid/provider/CallLog$Calls;": [
        "Landroid/provider/CallLog$Calls;->removeExpiredEntries(Landroid/content/Context;)",
    ],
    "Landroid/pim/vcard/VCardEntryHandler;": [
        "Landroid/pim/vcard/VCardEntryHandler;->onEntryCreated(Landroid/pim/vcard/VCardEntry;)",
    ],
    "Landroid/provider/Contacts$People;": [
        "Landroid/provider/Contacts$People;->addToGroup(Landroid/content/ContentResolver;JJ)",
    ],
    "Landroid/provider/ContactsContract$Contacts;": [
        "Landroid/provider/ContactsContract$Contacts;->markAsContacted(Landroid/content/ContentResolver;J)",
    ],
},
"android.permission.READ_CONTACTS": {
    "Landroid/provider/ContactsContract$Data;": [
        "Landroid/provider/ContactsContract$Data;->getContactLookupUri(Landroid/content/ContentResolver;Landroid/net/Uri;)",
    ],
    "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;": [
        "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;->getAdnRecordsInEf(I)",
    ],
    "Landroid/pim/vcard/VCardComposer$OneEntryHandler;": [
        "Landroid/pim/vcard/VCardComposer$OneEntryHandler;->onInit(Landroid/content/Context;)",
    ],
    "Lcom/android/internal/telephony/CallerInfo;": [
        "Lcom/android/internal/telephony/CallerInfo;->getCallerId(Landroid/content/Context;Ljava/lang/String;)",
        "Lcom/android/internal/telephony/CallerInfo;->getCallerInfo(Landroid/content/Context;Ljava/lang/String;)",
    ],
    "Landroid/provider/Contacts$Settings;": [
        "Landroid/provider/Contacts$Settings;->getSetting(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)",
    ],
    "Landroid/provider/Contacts$People;": [
        "Landroid/provider/Contacts$People;->addToGroup(Landroid/content/ContentResolver;JLjava/lang/String;)",
        "Landroid/provider/Contacts$People;->addToMyContactsGroup(Landroid/content/ContentResolver;J)",
        "Landroid/provider/Contacts$People;->createPersonInMyContactsGroup(Landroid/content/ContentResolver;Landroid/content/ContentValues;)",
        "Landroid/provider/Contacts$People;->loadContactPhoto(Landroid/content/Context;Landroid/net/Uri;ILandroid/graphics/BitmapFactory$Options;)",
        "Landroid/provider/Contacts$People;->markAsContacted(Landroid/content/ContentResolver;J)",
        "Landroid/provider/Contacts$People;->openContactPhotoInputStream(Landroid/content/ContentResolver;Landroid/net/Uri;)",
        "Landroid/provider/Contacts$People;->queryGroups(Landroid/content/ContentResolver;J)",
        "Landroid/provider/Contacts$People;->setPhotoData(Landroid/content/ContentResolver;Landroid/net/Uri;L[B;)",
        "Landroid/provider/Contacts$People;->tryGetMyContactsGroupId(Landroid/content/ContentResolver;)",
    ],
    "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;": [
        "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;->getAdnRecordsInEf(I)",
    ],
    "Landroid/widget/QuickContactBadge;": [
        "Landroid/widget/QuickContactBadge;->assignContactFromEmail(Ljava/lang/String;Z)",
        "Landroid/widget/QuickContactBadge;->assignContactFromPhone(Ljava/lang/String;Z)",
        "Landroid/widget/QuickContactBadge;->trigger(Landroid/net/Uri;)",
    ],
    "Landroid/provider/ContactsContract$RawContacts;": [
        "Landroid/provider/ContactsContract$RawContacts;->getContactLookupUri(Landroid/content/ContentResolver;Landroid/net/Uri;)",
    ],
    "Landroid/app/ContextImpl$ApplicationContentResolver;": [
        "Landroid/app/ContextImpl$ApplicationContentResolver;->openFileDescriptor(Landroid/net/Uri;Ljava/lang/String;)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->openInputStream(Landroid/net/Uri;)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->openOutputStream(Landroid/net/Uri;)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->query(Landroid/net/Uri;L[Ljava/lang/String;;Ljava/lang/String;L[Ljava/lang/String;;Ljava/lang/String;)",
    ],
    "Landroid/provider/CallLog$Calls;": [
        "Landroid/provider/CallLog$Calls;->addCall(Lcom/android/internal/telephony/CallerInfo;Landroid/content/Context;Ljava/lang/String;IIJI)",
        "Landroid/provider/CallLog$Calls;->getLastOutgoingCall(Landroid/content/Context;)",
    ],
    "Landroid/content/ContentResolver;": [
        "Landroid/content/ContentResolver;->openFileDescriptor(Landroid/net/Uri;Ljava/lang/String;)",
        "Landroid/content/ContentResolver;->openInputStream(Landroid/net/Uri;)",
        "Landroid/content/ContentResolver;->openOutputStream(Landroid/net/Uri;)",
        "Landroid/content/ContentResolver;->query(Landroid/net/Uri;L[Ljava/lang/String;;Ljava/lang/String;L[Ljava/lang/String;;Ljava/lang/String;)",
    ],
    "Landroid/pim/vcard/VCardComposer$HandlerForOutputStream;": [
        "Landroid/pim/vcard/VCardComposer$HandlerForOutputStream;->onInit(Landroid/content/Context;)",
    ],
    "Landroid/pim/vcard/VCardComposer;": [
        "Landroid/pim/vcard/VCardComposer;->createOneEntry(L;)",
        "Landroid/pim/vcard/VCardComposer;->createOneEntry(Ljava/lang/reflect/Method;)",
        "Landroid/pim/vcard/VCardComposer;->createOneEntryInternal(Ljava/lang/String;Ljava/lang/reflect/Method;)",
        "Landroid/pim/vcard/VCardComposer;->init(L;)",
        "Landroid/pim/vcard/VCardComposer;->init(Ljava/lang/String;L[Ljava/lang/String;;)",
    ],
    "Landroid/provider/ContactsContract$Contacts;": [
        "Landroid/provider/ContactsContract$Contacts;->getLookupUri(Landroid/content/ContentResolver;Landroid/net/Uri;)",
        "Landroid/provider/ContactsContract$Contacts;->lookupContact(Landroid/content/ContentResolver;Landroid/net/Uri;)",
        "Landroid/provider/ContactsContract$Contacts;->openContactPhotoInputStream(Landroid/content/ContentResolver;Landroid/net/Uri;)",
    ],
},
"android.permission.BIND_APPWIDGET": {
    "Landroid/appwidget/AppWidgetManager;": [
        "Landroid/appwidget/AppWidgetManager;->bindAppWidgetId(ILandroid/content/ComponentName;)",
    ],
    "Lcom/android/internal/appwidget/IAppWidgetService$Stub$Proxy;": [
        "Lcom/android/internal/appwidget/IAppWidgetService$Stub$Proxy;->bindAppWidgetId(ILComponentName;)",
    ],
},
"android.permission.SIGNAL_PERSISTENT_PROCESSES": {
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->signalPersistentProcesses(I)",
    ],
},
"android.permission.ASEC_CREATE": {
    "Landroid/os/storage/IMountService$Stub$Proxy;": [
        "Landroid/os/storage/IMountService$Stub$Proxy;->createSecureContainer(Ljava/lang/String;ILjava/lang/String;Ljava/lang/String;I)",
        "Landroid/os/storage/IMountService$Stub$Proxy;->finalizeSecureContainer(Ljava/lang/String;)",
    ],
},
"android.permission.INSTALL_LOCATION_PROVIDER": {
    "Landroid/location/ILocationManager$Stub$Proxy;": [
        "Landroid/location/ILocationManager$Stub$Proxy;->reportLocation(Landroid/location/Location;Z)",
    ],
},
"android.permission.WRITE_SETTINGS": {
    "Landroid/os/IPowerManager$Stub$Proxy;": [
        "Landroid/os/IPowerManager$Stub$Proxy;->setStayOnSetting(I)",
    ],
    "Landroid/provider/Settings$Bookmarks;": [
        "Landroid/provider/Settings$Bookmarks;->add(Landroid/content/ContentResolver;Landroid/content/Intent;Ljava/lang/String;Ljava/lang/String;CI)",
        "Landroid/provider/Settings$Bookmarks;->getIntentForShortcut(Landroid/content/ContentResolver;C)",
    ],
    "Landroid/server/BluetoothService;": [
        "Landroid/server/BluetoothService;->persistBluetoothOnSetting(Z)",
    ],
    "Landroid/os/IMountService$Stub$Proxy;": [
        "Landroid/os/IMountService$Stub$Proxy;->setAutoStartUm(Landroid/os/IMountService$Stub$Proxy/setAutoStartUm;)",
        "Landroid/os/IMountService$Stub$Proxy;->setPlayNotificationSound(Landroid/os/IMountService$Stub$Proxy/setPlayNotificationSound;)",
    ],
    "Landroid/provider/Settings$System;": [
        "Landroid/provider/Settings$System;->putConfiguration(Landroid/content/ContentResolver;Landroid/content/res/Configuration;)",
        "Landroid/provider/Settings$System;->putFloat(Landroid/content/ContentResolver;Ljava/lang/String;F)",
        "Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)",
        "Landroid/provider/Settings$System;->putLong(Landroid/content/ContentResolver;Ljava/lang/String;J)",
        "Landroid/provider/Settings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/provider/Settings$System;->setShowGTalkServiceStatus(Landroid/content/ContentResolver;Z)",
    ],
    "Landroid/media/RingtoneManager;": [
        "Landroid/media/RingtoneManager;->setActualDefaultRingtoneUri(Landroid/content/Context;ILandroid/net/Uri;)",
    ],
    "Landroid/provider/Settings$Secure;": [
        "Landroid/provider/Settings$Secure;->putFloat(Landroid/content/ContentResolver;Ljava/lang/String;F)",
        "Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)",
        "Landroid/provider/Settings$Secure;->putLong(Landroid/content/ContentResolver;Ljava/lang/String;J)",
        "Landroid/provider/Settings$Secure;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/provider/Settings$Secure;->setLocationProviderEnabled(Landroid/content/ContentResolver;Ljava/lang/String;Z)",
    ],
},
"android.permission.READ_INPUT_STATE": {
    "Landroid/view/IWindowManager$Stub$Proxy;": [
        "Landroid/view/IWindowManager$Stub$Proxy;->getDPadKeycodeState(I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->getDPadScancodeState(I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->getKeycodeState(I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->getKeycodeStateForDevice(II)",
        "Landroid/view/IWindowManager$Stub$Proxy;->getScancodeState(I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->getScancodeStateForDevice(II)",
        "Landroid/view/IWindowManager$Stub$Proxy;->getSwitchState(I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->getSwitchStateForDevice(II)",
        "Landroid/view/IWindowManager$Stub$Proxy;->getTrackballKeycodeState(I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->getTrackballScancodeState(I)",
    ],
},
"android.permission.MANAGE_APP_TOKENS": {
    "Landroid/view/IWindowManager$Stub$Proxy;": [
        "Landroid/view/IWindowManager$Stub$Proxy;->addAppToken(ILandroid/view/IApplicationToken;IIZ)",
        "Landroid/view/IWindowManager$Stub$Proxy;->addWindowToken(Landroid/os/IBinder;I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->executeAppTransition(L;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->moveAppToken(ILandroid/os/IBinder;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->moveAppTokensToBottom(Ljava/util/List;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->moveAppTokensToTop(Ljava/util/List;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->pauseKeyDispatching(Landroid/os/IBinder;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->prepareAppTransition(I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->removeAppToken(Landroid/os/IBinder;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->removeWindowToken(Landroid/os/IBinder;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->resumeKeyDispatching(Landroid/os/IBinder;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->setAppGroupId(Landroid/os/IBinder;I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->setAppOrientation(Landroid/view/IApplicationToken;I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->setAppStartingWindow(Landroid/os/IBinder;Ljava/lang/String;ILjava/lang/CharSequence;IILandroid/os/IBinder;Z)",
        "Landroid/view/IWindowManager$Stub$Proxy;->setAppVisibility(Landroid/os/IBinder;Z)",
        "Landroid/view/IWindowManager$Stub$Proxy;->setAppWillBeHidden(Landroid/os/IBinder;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->setEventDispatching(Z)",
        "Landroid/view/IWindowManager$Stub$Proxy;->setFocusedApp(Landroid/os/IBinder;Z)",
        "Landroid/view/IWindowManager$Stub$Proxy;->setNewConfiguration(Landroid/content/res/Configuration;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->startAppFreezingScreen(Landroid/os/IBinder;I)",
        "Landroid/view/IWindowManager$Stub$Proxy;->stopAppFreezingScreen(Landroid/os/IBinder;Z)",
        "Landroid/view/IWindowManager$Stub$Proxy;->updateOrientationFromAppTokens(Landroid/content/res/Configuration;Landroid/os/IBinder;)",
    ],
},
"android.permission.ACCESS_WIMAX_STATE": {
    "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;": [
        "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;->getConnectionInf(Lcom/htc/net/wimax/WimaxController$Stub$Proxy/getConnectionInf;)",
        "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;->getWimaxStat(Lcom/htc/net/wimax/WimaxController$Stub$Proxy/getWimaxStat;)",
        "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;->isBackoffStat(Lcom/htc/net/wimax/WimaxController$Stub$Proxy/isBackoffStat;)",
        "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;->isWimaxEnable(Lcom/htc/net/wimax/WimaxController$Stub$Proxy/isWimaxEnable;)",
    ],
},
"android.permission.MODIFY_AUDIO_SETTINGS": {
    "Landroid/media/IAudioService$Stub$Proxy;": [
        "Landroid/media/IAudioService$Stub$Proxy;->setBluetoothScoOn(Z)",
        "Landroid/media/IAudioService$Stub$Proxy;->setMode(ILandroid/os/IBinder;)",
        "Landroid/media/IAudioService$Stub$Proxy;->setSpeakerphoneOn(Z)",
        "Landroid/media/IAudioService$Stub$Proxy;->startBluetoothSco(Landroid/os/IBinder;)",
        "Landroid/media/IAudioService$Stub$Proxy;->stopBluetoothSco(Landroid/os/IBinder;)",
    ],
    "Landroid/server/BluetoothA2dpService;": [
        "Landroid/server/BluetoothA2dpService;->checkSinkSuspendState(I)",
        "Landroid/server/BluetoothA2dpService;->handleSinkStateChange(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/server/BluetoothA2dpService;->onBluetoothDisable(L;)",
        "Landroid/server/BluetoothA2dpService;->onBluetoothEnable(L;)",
    ],
    "Landroid/media/AudioService;": [
        "Landroid/media/AudioService;->setBluetoothScoOn(Z)",
        "Landroid/media/AudioService;->setMode(ILandroid/os/IBinder;)",
        "Landroid/media/AudioService;->setSpeakerphoneOn(Z)",
        "Landroid/media/AudioService;->startBluetoothSco(Landroid/os/IBinder;)",
        "Landroid/media/AudioService;->stopBluetoothSco(Landroid/os/IBinder;)",
    ],
    "Landroid/media/AudioManager;": [
        "Landroid/media/AudioManager;->isBluetoothA2dpOn(L;)",
        "Landroid/media/AudioManager;->isWiredHeadsetOn(L;)",
        "Landroid/media/AudioManager;->setBluetoothScoOn(Z)",
        "Landroid/media/AudioManager;->setMicrophoneMute(Z)",
        "Landroid/media/AudioManager;->setMode(I)",
        "Landroid/media/AudioManager;->setParameter(Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/media/AudioManager;->setParameters(Ljava/lang/String;)",
        "Landroid/media/AudioManager;->setSpeakerphoneOn(Z)",
        "Landroid/media/AudioManager;->startBluetoothSco(L;)",
        "Landroid/media/AudioManager;->stopBluetoothSco(L;)",
    ],
},
"android.permission.ACCESS_SURFACE_FLINGER": {
    "Landroid/view/Surface;": [
        "Landroid/view/Surface;->closeTransaction(L;)",
        "Landroid/view/Surface;->freezeDisplay(I)",
        "Landroid/view/Surface;->setOrientation(III)",
        "Landroid/view/Surface;->setOrientation(II)",
        "Landroid/view/Surface;->unfreezeDisplay(I)",
    ],
    "Landroid/view/SurfaceSession;": [
        "Landroid/view/SurfaceSession;-><init>(L;)",
    ],
},
"android.permission.CHANGE_BACKGROUND_DATA_SETTING": {
    "Landroid/net/ConnectivityManager;": [
        "Landroid/net/ConnectivityManager;->setBackgroundDataSetting(Z)",
    ],
    "Landroid/net/IConnectivityManager$Stub$Proxy;": [
        "Landroid/net/IConnectivityManager$Stub$Proxy;->setBackgroundDataSetting(Z)",
    ],
},
"android.permission.CALL_PRIVILEGED": {
    "Landroid/telephony/PhoneNumberUtils;": [
        "Landroid/telephony/PhoneNumberUtils;->getNumberFromIntent(Landroid/content/Intent;Landroid/content/Context;)",
    ],
    "Landroid/telephony/TelephonyManager;": [
        "Landroid/telephony/TelephonyManager;->getCompleteVoiceMailNumber(L;)",
    ],
},
"android.permission.WRITE_CALENDAR": {
    "Landroid/provider/Calendar$Calendars;": [
        "Landroid/provider/Calendar$Calendars;->delete(Landroid/content/ContentResolver;Ljava/lang/String;L[Ljava/lang/String;;)",
        "Landroid/provider/Calendar$Calendars;->deleteCalendarsForAccount(Landroid/content/ContentResolver;Landroid/accounts/Account;)",
    ],
    "Landroid/provider/Calendar$CalendarAlerts;": [
        "Landroid/provider/Calendar$CalendarAlerts;->insert(Landroid/content/ContentResolver;JJJJI)",
    ],
},
"android.permission.MANAGE_ACCOUNTS": {
    "Landroid/accounts/AccountManager;": [
        "Landroid/accounts/AccountManager;->addAccount(Ljava/lang/String;Ljava/lang/String;L[Ljava/lang/String;;Landroid/os/Bundle;Landroid/app/Activity;Landroid/accounts/AccountManagerCallback;Landroid/os/Handler;)",
        "Landroid/accounts/AccountManager;->clearPassword(Landroid/accounts/Account;)",
        "Landroid/accounts/AccountManager;->confirmCredentials(Landroid/accounts/Account;Landroid/os/Bundle;Landroid/app/Activity;Landroid/accounts/AccountManagerCallback;Landroid/os/Handler;)",
        "Landroid/accounts/AccountManager;->editProperties(Ljava/lang/String;Landroid/app/Activity;Landroid/accounts/AccountManagerCallback;Landroid/os/Handler;)",
        "Landroid/accounts/AccountManager;->invalidateAuthToken(Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/accounts/AccountManager;->removeAccount(Landroid/accounts/Account;Landroid/accounts/AccountManagerCallback;Landroid/os/Handler;)",
        "Landroid/accounts/AccountManager;->updateCredentials(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;Landroid/app/Activity;Landroid/accounts/AccountManagerCallback;Landroid/os/Handler;)",
    ],
    "Landroid/accounts/IAccountManager$Stub$Proxy;": [
        "Landroid/accounts/IAccountManager$Stub$Proxy;->addAcount(Landroid/accounts/IAccountManagerResponse;Ljava/lang/String;Ljava/lang/String;L[Ljava/lang/String;;ZLandroid/os/Bundle;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->clearPassword(Landroid/accounts/Account;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->confirmCredentials(Landroid/accounts/IAccountManagerResponse;Landroid/accounts/Account;Landroid/os/Bundle;Z)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->editProperties(Landroid/accounts/IAccountManagerResponse;Ljava/lang/String;Z)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->invalidateAuthToken(Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->removeAccount(Landroid/accounts/IAccountManagerResponse;Landroid/accounts/Account;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->updateCredentials(Landroid/accounts/IAccountManagerResponse;Landroid/accounts/Account;Ljava/lang/String;ZLandroid/os/Bundle;)",
    ],
    "Landroid/accounts/AccountManagerService;": [
        "Landroid/accounts/AccountManagerService;->addAcount(Landroid/accounts/IAccountManagerResponse;Ljava/lang/String;Ljava/lang/String;L[Ljava/lang/String;;ZLandroid/os/Bundle;)",
        "Landroid/accounts/AccountManagerService;->checkManageAccountsOrUseCredentialsPermissions(L;)",
        "Landroid/accounts/AccountManagerService;->checkManageAccountsPermission(L;)",
        "Landroid/accounts/AccountManagerService;->clearPassword(Landroid/accounts/Account;)",
        "Landroid/accounts/AccountManagerService;->confirmCredentials(Landroid/accounts/IAccountManagerResponse;Landroid/accounts/Account;Landroid/os/Bundle;Z)",
        "Landroid/accounts/AccountManagerService;->editProperties(Landroid/accounts/IAccountManagerResponse;Ljava/lang/String;Z)",
        "Landroid/accounts/AccountManagerService;->invalidateAuthToken(Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/accounts/AccountManagerService;->removeAccount(Landroid/accounts/IAccountManagerResponse;Landroid/accounts/Account;)",
        "Landroid/accounts/AccountManagerService;->updateCredentials(Landroid/accounts/IAccountManagerResponse;Landroid/accounts/Account;Ljava/lang/String;ZLandroid/os/Bundle;)",
    ],
},
"android.permission.SEND_SMS": {
    "Landroid/telephony/SmsManager;": [
        "Landroid/telephony/SmsManager;->sendDataMessage(Ljava/lang/String;Ljava/lang/String;SL[B;Landroid/app/PendingIntent;Landroid/app/PendingIntent;)",
        "Landroid/telephony/SmsManager;->sendMultipartTextMessage(Ljava/lang/String;Ljava/lang/String;Ljava/util/ArrayList;Ljava/util/ArrayList;Ljava/util/ArrayList;)",
        "Landroid/telephony/SmsManager;->sendTextMessage(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/app/PendingIntent;Landroid/app/PendingIntent;)",
    ],
    "Lcom/android/internal/telephony/ISms$Stub$Proxy;": [
        "Lcom/android/internal/telephony/ISms$Stub$Proxy;->sendData(Ljava/lang/String;Ljava/lang/String;I[BLandroid/app/PendingIntent;Landroid/app/PendingIntent;)",
        "Lcom/android/internal/telephony/ISms$Stub$Proxy;->sendMultipartText(Ljava/lang/String;Ljava/lang/String;Ljava/util/List;Ljava/util/List;Ljava/util/List;)",
        "Lcom/android/internal/telephony/ISms$Stub$Proxy;->sendText(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/app/PendingIntent;Landroid/app/PendingIntent;)",
    ],
    "Landroid/telephony/gsm/SmsManager;": [
        "Landroid/telephony/gsm/SmsManager;->sendDataMessage(Ljava/lang/String;Ljava/lang/String;SL[B;Landroid/app/PendingIntent;Landroid/app/PendingIntent;)",
        "Landroid/telephony/gsm/SmsManager;->sendMultipartTextMessage(Ljava/lang/String;Ljava/lang/String;Ljava/util/ArrayList;Ljava/util/ArrayList;Ljava/util/ArrayList;)",
        "Landroid/telephony/gsm/SmsManager;->sendTextMessage(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Landroid/app/PendingIntent;Landroid/app/PendingIntent;)",
    ],
},
"android.permission.ACCESS_MOCK_LOCATION": {
    "Landroid/location/LocationManager;": [
        "Landroid/location/LocationManager;->addTestProvider(Ljava/lang/String;ZZZZZZZII)",
        "Landroid/location/LocationManager;->clearTestProviderEnabled(Ljava/lang/String;)",
        "Landroid/location/LocationManager;->clearTestProviderLocation(Ljava/lang/String;)",
        "Landroid/location/LocationManager;->clearTestProviderStatus(Ljava/lang/String;)",
        "Landroid/location/LocationManager;->removeTestProvider(Ljava/lang/String;)",
        "Landroid/location/LocationManager;->setTestProviderEnabled(Ljava/lang/String;Z)",
        "Landroid/location/LocationManager;->setTestProviderLocation(Ljava/lang/String;Landroid/location/Location;)",
        "Landroid/location/LocationManager;->setTestProviderStatus(Ljava/lang/String;ILandroid/os/Bundle;J)",
    ],
    "Landroid/location/ILocationManager$Stub$Proxy;": [
        "Landroid/location/ILocationManager$Stub$Proxy;->addTestProvider(Ljava/lang/String;ZZZZZZZII)",
        "Landroid/location/ILocationManager$Stub$Proxy;->clearTestProviderEnabled(Ljava/lang/String;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->clearTestProviderLocation(Ljava/lang/String;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->clearTestProviderStatus(Ljava/lang/String;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->removeTestProvider(Ljava/lang/String;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->setTestProviderEnabled(Ljava/lang/String;Z)",
        "Landroid/location/ILocationManager$Stub$Proxy;->setTestProviderLocation(Ljava/lang/String;Landroid/location/Location;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->setTestProviderStatus(Ljava/lang/String;ILandroid/os/Bundle;J)",
    ],
},
"android.permission.WRITE_SMS": {
    "Landroid/provider/Telephony$Sms$Outbox;": [
        "Landroid/provider/Telephony$Sms$Outbox;->addMessage(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Long;ZJ)",
    ],
    "Landroid/provider/Telephony$Sms;": [
        "Landroid/provider/Telephony$Sms;->addMessageToUri(Landroid/content/ContentResolver;Landroid/net/Uri;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Long;ZZJ)",
        "Landroid/provider/Telephony$Sms;->addMessageToUri(Landroid/content/ContentResolver;Landroid/net/Uri;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Long;ZZ)",
        "Landroid/provider/Telephony$Sms;->moveMessageToFolder(Landroid/content/Context;Landroid/net/Uri;II)",
    ],
    "Landroid/provider/Telephony$Sms$Draft;": [
        "Landroid/provider/Telephony$Sms$Draft;->saveMessage(Landroid/content/ContentResolver;Landroid/net/Uri;Ljava/lang/String;)",
    ],
},
"android.permission.GET_TASKS": {
    "Landroid/app/ActivityManager;": [
        "Landroid/app/ActivityManager;->getRecentTasks(II)",
        "Landroid/app/ActivityManager;->getRunningTasks(I)",
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->getRecentTasks(II)",
        "Landroid/app/IActivityManager$Stub$Proxy;->getTasks(IILandroid/app/IThumbnailReceiver;)",
    ],
    "Landroid/app/ActivityManagerNative;": [
        "Landroid/app/ActivityManagerNative;->getRecentTasks(II)",
        "Landroid/app/ActivityManagerNative;->getRunningTasks(I)",
    ],
},
"android.permission.DELETE_PACKAGES": {
    "Landroid/app/ContextImpl$ApplicationPackageManager;": [
        "Landroid/app/ContextImpl$ApplicationPackageManager;->deletePackage(LString;LIPackageDeleteObserver;I)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->deletePackage(Ljava/lang/String;LIPackageDeleteObserver;I)",
    ],
    "Landroid/content/pm/PackageManager;": [
        "Landroid/content/pm/PackageManager;->deletePackage(Ljava/lang/String;LIPackageDeleteObserver;I)",
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->deletePackage(Ljava/lang/String;Landroid/content/pm/IPackageDeleteObserver;I)",
    ],
},
"android.permission.SET_PREFERRED_APPLICATIONS": {
    "Landroid/app/ContextImpl$ApplicationPackageManager;": [
        "Landroid/app/ContextImpl$ApplicationPackageManager;->addPreferredActivity(LIntentFilter;I[LComponentName;LComponentName;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->clearPackagePreferredActivities(LString;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->replacePreferredActivity(LIntentFilter;I[LComponentName;LComponentName;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->addPreferredActivity(Landroid/content/IntentFilter;I[Landroid/content/ComponentName;Landroid/content/ComponentName;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->clearPackagePreferredActivities(Ljava/lang/String;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->replacePreferredActivity(Landroid/content/IntentFilter;I[Landroid/content/ComponentName;Landroid/content/ComponentName;)",
    ],
    "Landroid/content/pm/PackageManager;": [
        "Landroid/content/pm/PackageManager;->addPreferredActivity(Landroid/content/IntentFilter;I[Landroid/content/ComponentName;Landroid/content/ComponentName;)",
        "Landroid/content/pm/PackageManager;->clearPackagePreferredActivities(Ljava/lang/String;)",
        "Landroid/content/pm/PackageManager;->replacePreferredActivity(Landroid/content/IntentFilter;I[Landroid/content/ComponentName;Landroid/content/ComponentName;)",
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->addPreferredActivity(Landroid/content/IntentFilter;IL[Landroid/content/ComponentName;;Landroid/content/ComponentName;)",
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->clearPackagePreferredActivities(Ljava/lang/String;)",
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->replacePreferredActivity(Landroid/content/IntentFilter;IL[Landroid/content/ComponentName;;Landroid/content/ComponentName;)",
    ],
},
"android.permission.SET_TIME": {
    "Landroid/app/IAlarmManager$Stub$Proxy;": [
        "Landroid/app/IAlarmManager$Stub$Proxy;->setTime(J)",
    ],
    "Landroid/app/AlarmManager;": [
        "Landroid/app/AlarmManager;->setTime(J)",
    ],
},
"android.permission.BATTERY_STATS": {
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;": [
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->getAwakeTimeBattery(L;)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->getAwakeTimePlugged(L;)",
        "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;->getStatistics(L;)",
    ],
},
"int)": {
    "Lcom/android/internal/app/IUsageStats$Stub$Proxy;": [
        "Lcom/android/internal/app/IUsageStats$Stub$Proxy;->noteLaunchTime(LComponentName;)",
    ],
},
"android.permission.CALL_PHONE": {
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;": [
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->call(Ljava/lang/String;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->endCall(L;)",
    ],
},
"android.permission.FLASHLIGHT": {
    "Landroid/os/IHardwareService$Stub$Proxy;": [
        "Landroid/os/IHardwareService$Stub$Proxy;->setFlashlightEnabled(Z)",
    ],
},
"android.permission.READ_PHONE_STATE": {
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;": [
        "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;->listen(Ljava/lang/String;Lcom/android/internal/telephony/IPhoneStateListener;IZ)",
    ],
    "Landroid/telephony/PhoneNumberUtils;": [
        "Landroid/telephony/PhoneNumberUtils;->isVoiceMailNumber(Ljava/lang/String;)",
    ],
    "Lcom/android/internal/telephony/CallerInfo;": [
        "Lcom/android/internal/telephony/CallerInfo;->markAsVoiceMail(L;)",
    ],
    "Landroid/telephony/TelephonyManager;": [
        "Landroid/telephony/TelephonyManager;->getDeviceId(L;)",
        "Landroid/telephony/TelephonyManager;->getDeviceSoftwareVersion(L;)",
        "Landroid/telephony/TelephonyManager;->getLine1AlphaTag(L;)",
        "Landroid/telephony/TelephonyManager;->getLine1Number(L;)",
        "Landroid/telephony/TelephonyManager;->getSimSerialNumber(L;)",
        "Landroid/telephony/TelephonyManager;->getSubscriberId(L;)",
        "Landroid/telephony/TelephonyManager;->getVoiceMailAlphaTag(L;)",
        "Landroid/telephony/TelephonyManager;->getVoiceMailNumber(L;)",
        "Landroid/telephony/TelephonyManager;->listen(Landroid/telephony/PhoneStateListener;I)",
    ],
    "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;": [
        "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;->getDeviceId(L;)",
        "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;->getDeviceSvn(L;)",
        "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;->getIccSerialNumber(L;)",
        "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;->getLine1AlphaTag(L;)",
        "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;->getLine1Number(L;)",
        "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;->getSubscriberId(L;)",
        "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;->getVoiceMailAlphaTag(L;)",
        "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;->getVoiceMailNumber(L;)",
    ],
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;": [
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->isSimPinEnabled(L;)",
    ],
    "Landroid/accounts/AccountManagerService$SimWatcher;": [
        "Landroid/accounts/AccountManagerService$SimWatcher;->onReceive(Landroid/content/Context;Landroid/content/Intent;)",
    ],
},
"android.permission.CLEAR_APP_USER_DATA": {
    "Landroid/app/ActivityManager;": [
        "Landroid/app/ActivityManager;->clearApplicationUserData(Ljava/lang/String;Landroid/content/pm/IPackageDataObserver;)",
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->clearApplicationUserData(Ljava/lang/String;Landroid/content/pm/IPackageDataObserver;)",
    ],
    "Landroid/app/ActivityManagerNative;": [
        "Landroid/app/ActivityManagerNative;->clearApplicationUserData(Ljava/lang/String;Landroid/content/pm/IPackageDataObserver;)",
    ],
    "Landroid/app/ContextImpl$ApplicationPackageManager;": [
        "Landroid/app/ContextImpl$ApplicationPackageManager;->clearApplicationUserData(LString;LIPackageDataObserver;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->clearApplicationUserData(Ljava/lang/String;LIPackageDataObserver;)",
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->clearApplicationUserData(Ljava/lang/String;Landroid/content/pm/IPackageDataObserver;)",
    ],
    "Landroid/content/pm/PackageManager;": [
        "Landroid/content/pm/PackageManager;->clearApplicationUserData(Ljava/lang/String;LIPackageDataObserver;)",
    ],
},
"android.permission.KILL_BACKGROUND_PROCESSES": {
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->killBackgroundProcesses(Ljava/lang/String;)",
    ],
},
"android.permission.STOP_APP_SWITCHES": {
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->resumeAppSwitches(L;)",
        "Landroid/app/IActivityManager$Stub$Proxy;->stopAppSwitches(L;)",
    ],
},
"android.permission.ACCESS_WIFI_STATE": {
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;": [
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->getConfiguredNetworks(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->getConnectionInfo(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->getDhcpInfo(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->getNumAllowedChannels(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->getScanResults(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->getValidChannelCounts(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->getWifiApEnabledState(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->getWifiEnabledState(L;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->isMulticastEnabled(L;)",
    ],
    "Landroid/net/wifi/WifiManager;": [
        "Landroid/net/wifi/WifiManager;->getConfiguredNetworks(L;)",
        "Landroid/net/wifi/WifiManager;->getConnectionInfo(L;)",
        "Landroid/net/wifi/WifiManager;->getDhcpInfo(L;)",
        "Landroid/net/wifi/WifiManager;->getNumAllowedChannels(L;)",
        "Landroid/net/wifi/WifiManager;->getScanResults(L;)",
        "Landroid/net/wifi/WifiManager;->getValidChannelCounts(L;)",
        "Landroid/net/wifi/WifiManager;->getWifiApState(L;)",
        "Landroid/net/wifi/WifiManager;->getWifiState(L;)",
        "Landroid/net/wifi/WifiManager;->isMulticastEnabled(L;)",
        "Landroid/net/wifi/WifiManager;->isWifiApEnabled(L;)",
        "Landroid/net/wifi/WifiManager;->isWifiEnabled(L;)",
    ],
},
"android.permission.WAKE_LOCK": {
    "Landroid/os/IPowerManager$Stub$Proxy;": [
        "Landroid/os/IPowerManager$Stub$Proxy;->acquireWakeLock(ILandroid/os/IBinder;Ljava/lang/String;)",
        "Landroid/os/IPowerManager$Stub$Proxy;->releaseWakeLock(Landroid/os/IBinder;I)",
    ],
    "Landroid/os/PowerManager$WakeLock;": [
        "Landroid/os/PowerManager$WakeLock;->acquire(L;)",
        "Landroid/os/PowerManager$WakeLock;->acquire(J)",
        "Landroid/os/PowerManager$WakeLock;->release(L;)",
        "Landroid/os/PowerManager$WakeLock;->release(I)",
    ],
    "Landroid/net/wifi/WifiManager$WifiLock;": [
        "Landroid/net/wifi/WifiManager$WifiLock;->acquire(L;)",
        "Landroid/net/wifi/WifiManager$WifiLock;->finalize(L;)",
        "Landroid/net/wifi/WifiManager$WifiLock;->release(L;)",
    ],
    "Landroid/bluetooth/ScoSocket;": [
        "Landroid/bluetooth/ScoSocket;->acquireWakeLock(L;)",
        "Landroid/bluetooth/ScoSocket;->close(L;)",
        "Landroid/bluetooth/ScoSocket;->finalize(L;)",
        "Landroid/bluetooth/ScoSocket;->releaseWakeLock(L;)",
        "Landroid/bluetooth/ScoSocket;->releaseWakeLockNow(L;)",
    ],
    "Landroid/media/MediaPlayer;": [
        "Landroid/media/MediaPlayer;->start(L;)",
        "Landroid/media/MediaPlayer;->stayAwake(Z)",
        "Landroid/media/MediaPlayer;->stop(L;)",
    ],
    "Landroid/bluetooth/HeadsetBase;": [
        "Landroid/bluetooth/HeadsetBase;->acquireWakeLock(L;)",
        "Landroid/bluetooth/HeadsetBase;->finalize(L;)",
        "Landroid/bluetooth/HeadsetBase;->handleInput(Ljava/lang/String;)",
        "Landroid/bluetooth/HeadsetBase;->releaseWakeLock(L;)",
    ],
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;": [
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->acquireWifiLock(Landroid/os/IBinder;ILjava/lang/String;)",
        "Landroid/net/wifi/IWifiManager$Stub$Proxy;->releaseWifiLock(Landroid/os/IBinder;)",
    ],
    "Landroid/media/AsyncPlayer;": [
        "Landroid/media/AsyncPlayer;->acquireWakeLock(L;)",
        "Landroid/media/AsyncPlayer;->enqueueLocked(Landroid/media/AsyncPlayer$Command;)",
        "Landroid/media/AsyncPlayer;->play(Landroid/content/Context;Landroid/net/Uri;ZI)",
        "Landroid/media/AsyncPlayer;->releaseWakeLock(L;)",
        "Landroid/media/AsyncPlayer;->stop(L;)",
    ],
},
"android.permission.ACCESS_DOWNLOAD_MANAGER": {
    "Landroid/net/Downloads$ById;": [
        "Landroid/net/Downloads$ById;->deleteDownload(Landroid/content/Context;J)",
        "Landroid/net/Downloads$ById;->getMimeTypeForId(Landroid/content/Context;J)",
        "Landroid/net/Downloads$ById;->getStatus(Landroid/content/Context;J)",
        "Landroid/net/Downloads$ById;->openDownload(Landroid/content/Context;JLjava/lang/String;)",
        "Landroid/net/Downloads$ById;->openDownloadStream(Landroid/content/Context;J)",
        "Landroid/net/Downloads$ById;->startDownloadByUri(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;ZIZZLjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)",
    ],
    "Landroid/net/Downloads$DownloadBase;": [
        "Landroid/net/Downloads$DownloadBase;->startDownloadByUri(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;ZIZZLjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)",
    ],
    "Landroid/net/Downloads$ByUri;": [
        "Landroid/net/Downloads$ByUri;->getCurrentOtaDownloads(Landroid/content/Context;Ljava/lang/String;)",
        "Landroid/net/Downloads$ByUri;->getProgressCursor(Landroid/content/Context;J)",
        "Landroid/net/Downloads$ByUri;->getStatus(Landroid/content/Context;Ljava/lang/String;J)",
        "Landroid/net/Downloads$ByUri;->removeAllDownloadsByPackage(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/net/Downloads$ByUri;->startDownloadByUri(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;ZIZZLjava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)",
    ],
},
"android.permission.DELETE_CACHE_FILES": {
    "Landroid/app/ContextImpl$ApplicationPackageManager;": [
        "Landroid/app/ContextImpl$ApplicationPackageManager;->deleteApplicationCacheFiles(LString;LIPackageDataObserver;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->deleteApplicationCacheFiles(Ljava/lang/String;Landroid/content/pm/IPackageDataObserver;)",
    ],
    "Landroid/content/pm/PackageManager;": [
        "Landroid/content/pm/PackageManager;->deleteApplicationCacheFiles(Ljava/lang/String;Landroid/content/pm/IPackageDataObserver;)",
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->deleteApplicationCacheFiles(Ljava/lang/String;Landroid/content/pm/IPackageDataObserver;)",
    ],
},
"android.permission.RESTART_PACKAGES": {
    "Landroid/app/ActivityManager;": [
        "Landroid/app/ActivityManager;->killBackgroundProcesses(Ljava/lang/String;)",
        "Landroid/app/ActivityManager;->restartPackage(Ljava/lang/String;)",
    ],
    "Landroid/app/ActivityManagerNative;": [
        "Landroid/app/ActivityManagerNative;->killBackgroundProcesses(Ljava/lang/String;)",
        "Landroid/app/ActivityManagerNative;->restartPackage(Ljava/lang/String;)",
    ],
},
"android.permission.GET_ACCOUNTS": {
    "Landroid/accounts/AccountManagerService;": [
        "Landroid/accounts/AccountManagerService;->checkReadAccountsPermission(L;)",
        "Landroid/accounts/AccountManagerService;->getAccounts(Ljava/lang/String;)",
        "Landroid/accounts/AccountManagerService;->getAccountsByFeatures(Landroid/accounts/IAccountManagerResponse;Ljava/lang/String;L[Ljava/lang/String;;)",
        "Landroid/accounts/AccountManagerService;->hasFeatures(Landroid/accounts/IAccountManagerResponse;Landroid/accounts/Account;L[Ljava/lang/String;;)",
    ],
    "Landroid/accounts/AccountManager$GetAuthTokenByTypeAndFeaturesTask;": [
        "Landroid/accounts/AccountManager$GetAuthTokenByTypeAndFeaturesTask;->doWork(L;)",
        "Landroid/accounts/AccountManager$GetAuthTokenByTypeAndFeaturesTask;->start(L;)",
    ],
    "Landroid/accounts/AccountManager;": [
        "Landroid/accounts/AccountManager;->addOnAccountsUpdatedListener(Landroid/accounts/OnAccountsUpdateListener;Landroid/os/Handler;Z)",
        "Landroid/accounts/AccountManager;->getAccounts(L;)",
        "Landroid/accounts/AccountManager;->getAccountsByType(Ljava/lang/String;)",
        "Landroid/accounts/AccountManager;->getAccountsByTypeAndFeatures(Ljava/lang/String;L[Ljava/lang/String;;Landroid/accounts/AccountManagerCallback;Landroid/os/Handler;)",
        "Landroid/accounts/AccountManager;->getAuthTokenByFeatures(Ljava/lang/String;Ljava/lang/String;L[Ljava/lang/String;;Landroid/app/Activity;Landroid/os/Bundle;Landroid/os/Bundle;Landroid/accounts/AccountManagerCallback;Landroid/os/Handler;)",
        "Landroid/accounts/AccountManager;->hasFeatures(Landroid/accounts/Account;L[Ljava/lang/String;;Landroid/accounts/AccountManagerCallback;Landroid/os/Handler;)",
    ],
    "Landroid/accounts/AccountManager$AmsTask;": [
        "Landroid/accounts/AccountManager$AmsTask;->doWork(L;)",
        "Landroid/accounts/AccountManager$AmsTask;->start(L;)",
    ],
    "Landroid/accounts/IAccountManager$Stub$Proxy;": [
        "Landroid/accounts/IAccountManager$Stub$Proxy;->getAccounts(Ljava/lang/String;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->getAccountsByFeatures(Landroid/accounts/IAccountManagerResponse;Ljava/lang/String;L[Ljava/lang/String;;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->hasFeatures(Landroid/accounts/IAccountManagerResponse;Landroid/accounts/Account;L[Ljava/lang/String;;)",
    ],
    "Landroid/content/ContentService;": [
        "Landroid/content/ContentService;-><init>(Landroid/content/Context;Z)",
        "Landroid/content/ContentService;->main(Landroid/content/Context;Z)",
    ],
},
"android.permission.CHANGE_NETWORK_STATE": {
    "Landroid/os/INetworkManagementService$Stub$Proxy;": [
        "Landroid/os/INetworkManagementService$Stub$Proxy;->attachPppd(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->detachPppd(Ljava/lang/String;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->disableNat(Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->enableNat(Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->setAccessPoint(Landroid/net/wifi/WifiConfiguration;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->setInterfaceThrottle(Ljava/lang/String;II)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->setIpForwardingEnabled(Z)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->startAccessPoint(Landroid/net/wifi/WifiConfiguration;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->startUsbRNDIS(L;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->stopAccessPoint(L;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->stopTethering(L;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->stopUsbRNDIS(L;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->tetherInterface(Ljava/lang/String;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->unregisterObserver(Landroid/net/INetworkManagementEventObserver;)",
        "Landroid/os/INetworkManagementService$Stub$Proxy;->untetherInterface(Ljava/lang/String;)",
    ],
    "Landroid/net/ConnectivityManager;": [
        "Landroid/net/ConnectivityManager;->requestRouteToHost(II)",
        "Landroid/net/ConnectivityManager;->setMobileDataEnabled(Z)",
        "Landroid/net/ConnectivityManager;->setNetworkPreference(I)",
        "Landroid/net/ConnectivityManager;->setRadio(IZ)",
        "Landroid/net/ConnectivityManager;->setRadios(Z)",
        "Landroid/net/ConnectivityManager;->startUsingNetworkFeature(ILjava/lang/String;)",
        "Landroid/net/ConnectivityManager;->stopUsingNetworkFeature(ILjava/lang/String;)",
        "Landroid/net/ConnectivityManager;->tether(Ljava/lang/String;)",
        "Landroid/net/ConnectivityManager;->untether(Ljava/lang/String;)",
    ],
    "Landroid/net/IConnectivityManager$Stub$Proxy;": [
        "Landroid/net/IConnectivityManager$Stub$Proxy;->requestRouteToHost(II)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->setMobileDataEnabled(Z)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->setNetworkPreference(I)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->setRadio(IZ)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->setRadios(Z)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->stopUsingNetworkFeature(ILjava/lang/String;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->tether(Ljava/lang/String;)",
        "Landroid/net/IConnectivityManager$Stub$Proxy;->untether(Ljava/lang/String;)",
    ],
},
"android.permission.READ_SYNC_SETTINGS": {
    "Landroid/app/ContextImpl$ApplicationContentResolver;": [
        "Landroid/app/ContextImpl$ApplicationContentResolver;->getIsSyncable(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->getMasterSyncAutomatically(L;)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->getPeriodicSyncs(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/app/ContextImpl$ApplicationContentResolver;->getSyncAutomatically(Landroid/accounts/Account;Ljava/lang/String;)",
    ],
    "Landroid/content/IContentService$Stub$Proxy;": [
        "Landroid/content/IContentService$Stub$Proxy;->getIsSyncable(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/IContentService$Stub$Proxy;->getMasterSyncAutomatically(L;)",
        "Landroid/content/IContentService$Stub$Proxy;->getPeriodicSyncs(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/IContentService$Stub$Proxy;->getSyncAutomatically(Landroid/accounts/Account;Ljava/lang/String;)",
    ],
    "Landroid/content/ContentService;": [
        "Landroid/content/ContentService;->getIsSyncable(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/ContentService;->getMasterSyncAutomatically(L;)",
        "Landroid/content/ContentService;->getPeriodicSyncs(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/ContentService;->getSyncAutomatically(Landroid/accounts/Account;Ljava/lang/String;)",
    ],
    "Landroid/content/ContentResolver;": [
        "Landroid/content/ContentResolver;->getIsSyncable(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/ContentResolver;->getMasterSyncAutomatically(L;)",
        "Landroid/content/ContentResolver;->getPeriodicSyncs(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/content/ContentResolver;->getSyncAutomatically(Landroid/accounts/Account;Ljava/lang/String;)",
    ],
},
"android.permission.DISABLE_KEYGUARD": {
    "Landroid/view/IWindowManager$Stub$Proxy;": [
        "Landroid/view/IWindowManager$Stub$Proxy;->disableKeyguard(Landroid/os/IBinder;Ljava/lang/String;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->exitKeyguardSecurely(Landroid/view/IOnKeyguardExitResult;)",
        "Landroid/view/IWindowManager$Stub$Proxy;->reenableKeyguard(Landroid/os/IBinder;)",
    ],
    "Landroid/app/KeyguardManager;": [
        "Landroid/app/KeyguardManager;->exitKeyguardSecurely(Landroid/app/KeyguardManager$OnKeyguardExitResult;)",
    ],
    "Landroid/app/KeyguardManager$KeyguardLock;": [
        "Landroid/app/KeyguardManager$KeyguardLock;->disableKeyguard(L;)",
        "Landroid/app/KeyguardManager$KeyguardLock;->reenableKeyguard(L;)",
    ],
},
"android.permission.USE_CREDENTIALS": {
    "Landroid/accounts/AccountManager;": [
        "Landroid/accounts/AccountManager;->blockingGetAuthToken(Landroid/accounts/Account;Ljava/lang/String;Z)",
        "Landroid/accounts/AccountManager;->getAuthToken(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;Landroid/app/Activity;Landroid/accounts/AccountManagerCallback;Landroid/os/Handler;)",
        "Landroid/accounts/AccountManager;->getAuthToken(Landroid/accounts/Account;Ljava/lang/String;ZLandroid/accounts/AccountManagerCallback;Landroid/os/Handler;)",
    ],
    "Landroid/accounts/IAccountManager$Stub$Proxy;": [
        "Landroid/accounts/IAccountManager$Stub$Proxy;->getAuthToken(Landroid/accounts/IAccountManagerResponse;Landroid/accounts/Account;Ljava/lang/String;ZZLandroid/os/Bundle;)",
    ],
    "Landroid/accounts/AccountManagerService;": [
        "Landroid/accounts/AccountManagerService;->getAuthToken(Landroid/accounts/IAccountManagerResponse;Landroid/accounts/Account;Ljava/lang/String;ZZLandroid/os/Bundle;)",
    ],
},
"android.permission.CHANGE_COMPONENT_ENABLED_STATE": {
    "Landroid/app/ContextImpl$ApplicationPackageManager;": [
        "Landroid/app/ContextImpl$ApplicationPackageManager;->setApplicationEnabledSetting(LString;II)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->setComponentEnabledSetting(LComponentName;II)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->setApplicationEnabledSetting(Ljava/lang/String;II)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->setComponentEnabledSetting(Landroid/content/ComponentName;II)",
    ],
    "Landroid/content/pm/PackageManager;": [
        "Landroid/content/pm/PackageManager;->setApplicationEnabledSetting(Ljava/lang/String;II)",
        "Landroid/content/pm/PackageManager;->setComponentEnabledSetting(Landroid/content/ComponentName;II)",
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->setApplicationEnabledSetting(Ljava/lang/String;II)",
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->setComponentEnabledSetting(Landroid/content/ComponentName;II)",
    ],
},
"android.permission.BACKUP": {
    "Landroid/app/backup/BackupManager;": [
        "Landroid/app/backup/BackupManager;->beginRestoreSession(L;)",
        "Landroid/app/backup/BackupManager;->dataChanged(Ljava/lang/String;)",
        "Landroid/app/backup/BackupManager;->requestRestore(Landroid/app/backup/RestoreObserver;)",
    ],
    "Landroid/app/backup/IBackupManager$Stub$Proxy;": [
        "Landroid/app/backup/IBackupManager$Stub$Proxy;->backupNow(L;)",
        "Landroid/app/backup/IBackupManager$Stub$Proxy;->beginRestoreSession(Ljava/lang/String;)",
        "Landroid/app/backup/IBackupManager$Stub$Proxy;->clearBackupData(Ljava/lang/String;)",
        "Landroid/app/backup/IBackupManager$Stub$Proxy;->dataChanged(Ljava/lang/String;)",
        "Landroid/app/backup/IBackupManager$Stub$Proxy;->getCurrentTransport(L;)",
        "Landroid/app/backup/IBackupManager$Stub$Proxy;->isBackupEnabled(L;)",
        "Landroid/app/backup/IBackupManager$Stub$Proxy;->listAllTransports(L;)",
        "Landroid/app/backup/IBackupManager$Stub$Proxy;->selectBackupTransport(Ljava/lang/String;)",
        "Landroid/app/backup/IBackupManager$Stub$Proxy;->setAutoRestore(Z)",
        "Landroid/app/backup/IBackupManager$Stub$Proxy;->setBackupEnabled(Z)",
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->bindBackupAgent(Landroid/content/pm/ApplicationInfo;I)",
    ],
},
"android.permission.EXPAND_STATUS_BAR": {
    "Landroid/app/IStatusBar$Stub$Proxy;": [
        "Landroid/app/IStatusBar$Stub$Proxy;->activate(L;)",
        "Landroid/app/IStatusBar$Stub$Proxy;->deactivate(L;)",
        "Landroid/app/IStatusBar$Stub$Proxy;->toggle(L;)",
    ],
    "Landroid/app/StatusBarManager;": [
        "Landroid/app/StatusBarManager;->collapse(L;)",
        "Landroid/app/StatusBarManager;->expand(L;)",
        "Landroid/app/StatusBarManager;->toggle(L;)",
    ],
},
"android.permission.BLUETOOTH_ADMIN": {
    "Landroid/bluetooth/BluetoothPbap;": [
        "Landroid/bluetooth/BluetoothPbap;->disconnect(L;)",
    ],
    "Landroid/server/BluetoothService;": [
        "Landroid/server/BluetoothService;->cancelBondProcess(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->cancelDiscovery(L;)",
        "Landroid/server/BluetoothService;->cancelPairingUserInput(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->createBond(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->disable(L;)",
        "Landroid/server/BluetoothService;->disable(Z)",
        "Landroid/server/BluetoothService;->enable(L;)",
        "Landroid/server/BluetoothService;->enable(Z)",
        "Landroid/server/BluetoothService;->removeBond(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->setDiscoverableTimeout(I)",
        "Landroid/server/BluetoothService;->setName(Ljava/lang/String;)",
        "Landroid/server/BluetoothService;->setPairingConfirmation(Ljava/lang/String;Z)",
        "Landroid/server/BluetoothService;->setPasskey(Ljava/lang/String;I)",
        "Landroid/server/BluetoothService;->setPin(Ljava/lang/String;L[B;)",
        "Landroid/server/BluetoothService;->setTrust(Ljava/lang/String;Z)",
        "Landroid/server/BluetoothService;->startDiscovery(L;)",
    ],
    "Landroid/bluetooth/BluetoothHeadset;": [
        "Landroid/bluetooth/BluetoothHeadset;->connectHeadset(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/BluetoothHeadset;->disconnectHeadset(L;)",
        "Landroid/bluetooth/BluetoothHeadset;->setPriority(Landroid/bluetooth/BluetoothDevice;I)",
    ],
    "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;": [
        "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;->connect(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;->disconnect(L;)",
    ],
    "Landroid/bluetooth/BluetoothAdapter;": [
        "Landroid/bluetooth/BluetoothAdapter;->cancelDiscovery(L;)",
        "Landroid/bluetooth/BluetoothAdapter;->disable(L;)",
        "Landroid/bluetooth/BluetoothAdapter;->enable(L;)",
        "Landroid/bluetooth/BluetoothAdapter;->setDiscoverableTimeout(I)",
        "Landroid/bluetooth/BluetoothAdapter;->setName(Ljava/lang/String;)",
        "Landroid/bluetooth/BluetoothAdapter;->startDiscovery(L;)",
    ],
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;": [
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->cancelBondProcess(Ljava/lang/String;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->cancelDiscovery(L;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->cancelPairingUserInput(Ljava/lang/String;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->createBond(Ljava/lang/String;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->disable(Z)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->enable(L;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->removeBond(Ljava/lang/String;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->setDiscoverableTimeout(I)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->setName(Ljava/lang/String;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->setPairingConfirmation(Ljava/lang/String;Z)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->setPasskey(Ljava/lang/String;I)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->setPin(Ljava/lang/String;L[B;)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->setTrust(Ljava/lang/String;Z)",
        "Landroid/bluetooth/IBluetooth$Stub$Proxy;->startDiscovery(L;)",
    ],
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;": [
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;->connectHeadset(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;->disconnectHeadset(L;)",
        "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;->setPriority(Landroid/bluetooth/BluetoothDevice;I)",
    ],
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;": [
        "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;->connectSink(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;->disconnectSink(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;->resumeSink(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;->setSinkPriority(Landroid/bluetooth/BluetoothDevice;I)",
        "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;->suspendSink(Landroid/bluetooth/BluetoothDevice;)",
    ],
    "Landroid/bluetooth/BluetoothDevice;": [
        "Landroid/bluetooth/BluetoothDevice;->cancelBondProcess(L;)",
        "Landroid/bluetooth/BluetoothDevice;->cancelPairingUserInput(L;)",
        "Landroid/bluetooth/BluetoothDevice;->createBond(L;)",
        "Landroid/bluetooth/BluetoothDevice;->removeBond(L;)",
        "Landroid/bluetooth/BluetoothDevice;->setPairingConfirmation(Z)",
        "Landroid/bluetooth/BluetoothDevice;->setPasskey(I)",
        "Landroid/bluetooth/BluetoothDevice;->setPin(L[B;)",
    ],
    "Landroid/bluetooth/BluetoothA2dp;": [
        "Landroid/bluetooth/BluetoothA2dp;->connectSink(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/BluetoothA2dp;->disconnectSink(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/BluetoothA2dp;->resumeSink(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/bluetooth/BluetoothA2dp;->setSinkPriority(Landroid/bluetooth/BluetoothDevice;I)",
        "Landroid/bluetooth/BluetoothA2dp;->suspendSink(Landroid/bluetooth/BluetoothDevice;)",
    ],
    "Landroid/server/BluetoothA2dpService;": [
        "Landroid/server/BluetoothA2dpService;->connectSink(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/server/BluetoothA2dpService;->disconnectSink(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/server/BluetoothA2dpService;->resumeSink(Landroid/bluetooth/BluetoothDevice;)",
        "Landroid/server/BluetoothA2dpService;->setSinkPriority(Landroid/bluetooth/BluetoothDevice;I)",
        "Landroid/server/BluetoothA2dpService;->setSinkPriority(Landroid/bluetooth/BluetoothDevice;I)",
        "Landroid/server/BluetoothA2dpService;->suspendSink(Landroid/bluetooth/BluetoothDevice;)",
    ],
},
"android.permission.ACCESS_FINE_LOCATION": {
    "Landroid/webkit/GeolocationPermissions$Callback;": [
        "Landroid/webkit/GeolocationPermissions$Callback;->invok(Landroid/webkit/GeolocationPermissions$Callback/invok;)",
    ],
    "Landroid/location/LocationManager;": [
        "Landroid/location/LocationManager;->_requestLocationUpdates(Ljava/lang/String;JFLandroid/app/PendingIntent;)",
        "Landroid/location/LocationManager;->_requestLocationUpdates(Ljava/lang/String;JFLandroid/location/LocationListener;Landroid/os/Looper;)",
        "Landroid/location/LocationManager;->addGpsStatusListener(Landroid/location/GpsStatus$Listener;)",
        "Landroid/location/LocationManager;->addNmeaListener(Landroid/location/GpsStatus$NmeaListener;)",
        "Landroid/location/LocationManager;->addProximityAlert(DDFJLandroid/app/PendingIntent;)",
        "Landroid/location/LocationManager;->best(Ljava/util/List;)",
        "Landroid/location/LocationManager;->getBestProvider(Landroid/location/Criteria;Z)",
        "Landroid/location/LocationManager;->getLastKnownLocation(Ljava/lang/String;)",
        "Landroid/location/LocationManager;->getProvider(Ljava/lang/String;)",
        "Landroid/location/LocationManager;->getProviders(Landroid/location/Criteria;Z)",
        "Landroid/location/LocationManager;->getProviders(Z)",
        "Landroid/location/LocationManager;->isProviderEnabled(Ljava/lang/String;)",
        "Landroid/location/LocationManager;->requestLocationUpdates(Ljava/lang/String;JFLandroid/app/PendingIntent;)",
        "Landroid/location/LocationManager;->requestLocationUpdates(Ljava/lang/String;JFLandroid/location/LocationListener;Landroid/os/Looper;)",
        "Landroid/location/LocationManager;->requestLocationUpdates(Ljava/lang/String;JFLandroid/location/LocationListener;)",
        "Landroid/location/LocationManager;->sendExtraCommand(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/location/ILocationManager$Stub$Proxy;": [
        "Landroid/location/ILocationManager$Stub$Proxy;->addGpsStatusListener(Landroid/location/IGpsStatusListener;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->addProximityAlert(DDFJLandroid/app/PendingIntent;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->getLastKnownLocation(Ljava/lang/String;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->getProviderInfo(Ljava/lang/String;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->getProviders(Z)",
        "Landroid/location/ILocationManager$Stub$Proxy;->isProviderEnabled(Ljava/lang/String;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->requestLocationUpdates(Ljava/lang/String;JFLandroid/location/ILocationListener;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->requestLocationUpdatesPI(Ljava/lang/String;JFLandroid/app/PendingIntent;)",
        "Landroid/location/ILocationManager$Stub$Proxy;->sendExtraCommand(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/telephony/TelephonyManager;": [
        "Landroid/telephony/TelephonyManager;->getCellLocation(L;)",
        "Landroid/telephony/TelephonyManager;->getNeighboringCellInfo(L;)",
    ],
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;": [
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->getCellLocation(L;)",
        "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;->getNeighboringCellInfo(L;)",
    ],
    "Landroid/webkit/WebChromeClient;": [
        "Landroid/webkit/WebChromeClient;->onGeolocationPermissionsShowPrompt(Ljava/lang/String;Landroid/webkit/GeolocationPermissions/Callback;)",
    ],
    "Landroid/webkit/GeolocationService;": [
        "Landroid/webkit/GeolocationService;->registerForLocationUpdates(L;)",
        "Landroid/webkit/GeolocationService;->setEnableGps(Z)",
        "Landroid/webkit/GeolocationService;->start(L;)",
    ],
},
"android.permission.ASEC_RENAME": {
    "Landroid/os/storage/IMountService$Stub$Proxy;": [
        "Landroid/os/storage/IMountService$Stub$Proxy;->renameSecureContainer(Ljava/lang/String;Ljava/lang/String;)",
    ],
},
"android.permission.PERSISTENT_ACTIVITY": {
    "Landroid/app/ExpandableListActivity;": [
        "Landroid/app/ExpandableListActivity;->setPersistent(Z)",
    ],
    "Landroid/app/TabActivity;": [
        "Landroid/app/TabActivity;->setPersistent(Z)",
    ],
    "Landroid/accounts/GrantCredentialsPermissionActivity;": [
        "Landroid/accounts/GrantCredentialsPermissionActivity;->setPersistent(Z)",
    ],
    "Landroid/app/AliasActivity;": [
        "Landroid/app/AliasActivity;->setPersistent(Z)",
    ],
    "Landroid/app/ActivityGroup;": [
        "Landroid/app/ActivityGroup;->setPersistent(Z)",
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->setPersistent(Landroid/os/IBinder;Z)",
    ],
    "Landroid/accounts/AccountAuthenticatorActivity;": [
        "Landroid/accounts/AccountAuthenticatorActivity;->setPersistent(Z)",
    ],
    "Landroid/app/Activity;": [
        "Landroid/app/Activity;->setPersistent(Z)",
    ],
    "Landroid/app/ListActivity;": [
        "Landroid/app/ListActivity;->setPersistent(Z)",
    ],
},
"android.permission.REORDER_TASKS": {
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->moveTaskBackwards(I)",
        "Landroid/app/IActivityManager$Stub$Proxy;->moveTaskToBack(I)",
        "Landroid/app/IActivityManager$Stub$Proxy;->moveTaskToFront(I)",
    ],
},
"android.permission.DEVICE_POWER": {
    "Landroid/os/IPowerManager$Stub$Proxy;": [
        "Landroid/os/IPowerManager$Stub$Proxy;->clearUserActivityTimeout(JJ)",
        "Landroid/os/IPowerManager$Stub$Proxy;->goToSleep(J)",
        "Landroid/os/IPowerManager$Stub$Proxy;->goToSleepWithReason(JI)",
        "Landroid/os/IPowerManager$Stub$Proxy;->preventScreenOn(Z)",
        "Landroid/os/IPowerManager$Stub$Proxy;->setAttentionLight(ZI)",
        "Landroid/os/IPowerManager$Stub$Proxy;->setBacklightBrightness(I)",
        "Landroid/os/IPowerManager$Stub$Proxy;->setPokeLock(ILandroid/os/IBinder;Ljava/lang/String;)",
        "Landroid/os/IPowerManager$Stub$Proxy;->userActivityWithForce(JZZ)",
    ],
    "Landroid/os/PowerManager;": [
        "Landroid/os/PowerManager;->goToSleep(J)",
        "Landroid/os/PowerManager;->setBacklightBrightness(I)",
    ],
},
"android.permission.SET_WALLPAPER": {
    "Landroid/app/Service;": [
        "Landroid/app/Service;->clearWallpaper(L;)",
        "Landroid/app/Service;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/Service;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/view/ContextThemeWrapper;": [
        "Landroid/view/ContextThemeWrapper;->clearWallpaper(L;)",
        "Landroid/view/ContextThemeWrapper;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/view/ContextThemeWrapper;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/content/Context;": [
        "Landroid/content/Context;->clearWallpaper(L;)",
        "Landroid/content/Context;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/content/Context;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/inputmethodservice/AbstractInputMethodService;": [
        "Landroid/inputmethodservice/AbstractInputMethodService;->clearWallpaper(L;)",
        "Landroid/inputmethodservice/AbstractInputMethodService;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/inputmethodservice/AbstractInputMethodService;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/ListActivity;": [
        "Landroid/app/ListActivity;->clearWallpaper(L;)",
        "Landroid/app/ListActivity;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/ListActivity;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/ExpandableListActivity;": [
        "Landroid/app/ExpandableListActivity;->clearWallpaper(L;)",
        "Landroid/app/ExpandableListActivity;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/ExpandableListActivity;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/TabActivity;": [
        "Landroid/app/TabActivity;->clearWallpaper(L;)",
        "Landroid/app/TabActivity;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/TabActivity;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/ActivityGroup;": [
        "Landroid/app/ActivityGroup;->clearWallpaper(L;)",
        "Landroid/app/ActivityGroup;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/ActivityGroup;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/ContextImpl;": [
        "Landroid/app/ContextImpl;->clearWallpaper(L;)",
        "Landroid/app/ContextImpl;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/ContextImpl;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/speech/RecognitionService;": [
        "Landroid/speech/RecognitionService;->clearWallpaper(L;)",
        "Landroid/speech/RecognitionService;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/speech/RecognitionService;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/IntentService;": [
        "Landroid/app/IntentService;->clearWallpaper(L;)",
        "Landroid/app/IntentService;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/IntentService;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/service/urlrenderer/UrlRendererService;": [
        "Landroid/service/urlrenderer/UrlRendererService;->clearWallpaper(L;)",
        "Landroid/service/urlrenderer/UrlRendererService;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/service/urlrenderer/UrlRendererService;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/backup/BackupAgent;": [
        "Landroid/app/backup/BackupAgent;->clearWallpaper(L;)",
        "Landroid/app/backup/BackupAgent;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/backup/BackupAgent;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/FullBackupAgent;": [
        "Landroid/app/FullBackupAgent;->clearWallpaper(L;)",
        "Landroid/app/FullBackupAgent;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/FullBackupAgent;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/backup/BackupAgentHelper;": [
        "Landroid/app/backup/BackupAgentHelper;->clearWallpaper(L;)",
        "Landroid/app/backup/BackupAgentHelper;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/backup/BackupAgentHelper;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/content/ContextWrapper;": [
        "Landroid/content/ContextWrapper;->clearWallpaper(L;)",
        "Landroid/content/ContextWrapper;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/content/ContextWrapper;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/accessibilityservice/AccessibilityService;": [
        "Landroid/accessibilityservice/AccessibilityService;->clearWallpaper(L;)",
        "Landroid/accessibilityservice/AccessibilityService;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/accessibilityservice/AccessibilityService;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/WallpaperManager;": [
        "Landroid/app/WallpaperManager;->clear(L;)",
        "Landroid/app/WallpaperManager;->setBitmap(Landroid/graphics/Bitmap;)",
        "Landroid/app/WallpaperManager;->setResource(I)",
        "Landroid/app/WallpaperManager;->setStream(Ljava/io/InputStream;)",
    ],
    "Landroid/app/AliasActivity;": [
        "Landroid/app/AliasActivity;->clearWallpaper(L;)",
        "Landroid/app/AliasActivity;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/AliasActivity;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/service/wallpaper/WallpaperService;": [
        "Landroid/service/wallpaper/WallpaperService;->clearWallpaper(L;)",
        "Landroid/service/wallpaper/WallpaperService;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/service/wallpaper/WallpaperService;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/IWallpaperManager$Stub$Proxy;": [
        "Landroid/app/IWallpaperManager$Stub$Proxy;->setWallpaper(Ljava/lang/String;)",
    ],
    "Landroid/app/Application;": [
        "Landroid/app/Application;->clearWallpaper(L;)",
        "Landroid/app/Application;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/Application;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/app/Activity;": [
        "Landroid/app/Activity;->clearWallpaper(L;)",
        "Landroid/app/Activity;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/app/Activity;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/content/MutableContextWrapper;": [
        "Landroid/content/MutableContextWrapper;->clearWallpaper(L;)",
        "Landroid/content/MutableContextWrapper;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/content/MutableContextWrapper;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/accounts/GrantCredentialsPermissionActivity;": [
        "Landroid/accounts/GrantCredentialsPermissionActivity;->clearWallpaper(L;)",
        "Landroid/accounts/GrantCredentialsPermissionActivity;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/accounts/GrantCredentialsPermissionActivity;->setWallpaper(Ljava/io/InputStream;)",
    ],
    "Landroid/accounts/AccountAuthenticatorActivity;": [
        "Landroid/accounts/AccountAuthenticatorActivity;->clearWallpaper(L;)",
        "Landroid/accounts/AccountAuthenticatorActivity;->setWallpaper(Landroid/graphics/Bitmap;)",
        "Landroid/accounts/AccountAuthenticatorActivity;->setWallpaper(Ljava/io/InputStream;)",
    ],
},
"android.permission.ASEC_DESTROY": {
    "Landroid/os/storage/IMountService$Stub$Proxy;": [
        "Landroid/os/storage/IMountService$Stub$Proxy;->destroySecureContainer(Ljava/lang/String;Z)",
    ],
},
"android.permission.GET_PACKAGE_SIZE": {
    "Landroid/app/ContextImpl$ApplicationPackageManager;": [
        "Landroid/app/ContextImpl$ApplicationPackageManager;->getPackageSizeInfo(LString;LIPackageStatsObserver;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->getPackageSizeInfo(Ljava/lang/String;Landroid/content/pm/IPackageStatsObserver;)",
    ],
    "Landroid/content/pm/PackageManager;": [
        "Landroid/content/pm/PackageManager;->getPackageSizeInfo(Ljava/lang/String;Landroid/content/pm/IPackageStatsObserver;)",
    ],
},
"android.permission.ASEC_MOUNT_UNMOUNT": {
    "Landroid/os/storage/IMountService$Stub$Proxy;": [
        "Landroid/os/storage/IMountService$Stub$Proxy;->mountSecureContainer(Ljava/lang/String;Ljava/lang/String;I)",
        "Landroid/os/storage/IMountService$Stub$Proxy;->unmountSecureContainer(Ljava/lang/String;Z)",
    ],
},
"android.permission.INSTALL_PACKAGES": {
    "Landroid/app/ContextImpl$ApplicationPackageManager;": [
        "Landroid/app/ContextImpl$ApplicationPackageManager;->installPackage(LUri;LIPackageInstallObserver;ILString;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->installPackage(LUri;LIPackageInstallObserver;ILjava/lang/String;)",
    ],
    "Landroid/content/pm/PackageManager;": [
        "Landroid/content/pm/PackageManager;->installPackage(LUri;LIPackageInstallObserver;ILjava/lang/String;)",
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->installPackage(Landroid/net/Uri;Landroid/content/pm/IPackageInstallObserver;ILjava/lang/String;)",
    ],
},
"android.permission.AUTHENTICATE_ACCOUNTS": {
    "Landroid/accounts/AccountManager;": [
        "Landroid/accounts/AccountManager;->addAccountExplicitly(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
        "Landroid/accounts/AccountManager;->getPassword(Landroid/accounts/Account;)",
        "Landroid/accounts/AccountManager;->getUserData(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/accounts/AccountManager;->peekAuthToken(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/accounts/AccountManager;->setAuthToken(Landroid/accounts/Account;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/accounts/AccountManager;->setPassword(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/accounts/AccountManager;->setUserData(Landroid/accounts/Account;Ljava/lang/String;Ljava/lang/String;)",
    ],
    "Landroid/accounts/IAccountManager$Stub$Proxy;": [
        "Landroid/accounts/IAccountManager$Stub$Proxy;->addAccount(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->getPassword(Landroid/accounts/Account;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->getUserData(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->peekAuthToken(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->setAuthToken(Landroid/accounts/Account;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->setPassword(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/accounts/IAccountManager$Stub$Proxy;->setUserData(Landroid/accounts/Account;Ljava/lang/String;Ljava/lang/String;)",
    ],
    "Landroid/accounts/AccountManagerService;": [
        "Landroid/accounts/AccountManagerService;->addAccount(Landroid/accounts/Account;Ljava/lang/String;Landroid/os/Bundle;)",
        "Landroid/accounts/AccountManagerService;->checkAuthenticateAccountsPermission(Landroid/accounts/Account;)",
        "Landroid/accounts/AccountManagerService;->getPassword(Landroid/accounts/Account;)",
        "Landroid/accounts/AccountManagerService;->getUserData(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/accounts/AccountManagerService;->peekAuthToken(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/accounts/AccountManagerService;->setAuthToken(Landroid/accounts/Account;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/accounts/AccountManagerService;->setPassword(Landroid/accounts/Account;Ljava/lang/String;)",
        "Landroid/accounts/AccountManagerService;->setUserData(Landroid/accounts/Account;Ljava/lang/String;Ljava/lang/String;)",
    ],
},
"android.permission.CLEAR_APP_CACHE": {
    "Landroid/app/ContextImpl$ApplicationPackageManager;": [
        "Landroid/app/ContextImpl$ApplicationPackageManager;->freeStorage(JLIntentSender;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->freeStorageAndNotify(JLIPackageDataObserver;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->freeStorage(JLandroid/content/IntentSender;)",
        "Landroid/app/ContextImpl$ApplicationPackageManager;->freeStorageAndNotify(JLandroid/content/pm/IPackageDataObserver;)",
    ],
    "Landroid/content/pm/PackageManager;": [
        "Landroid/content/pm/PackageManager;->freeStorage(JLandroid/content/IntentSender;)",
        "Landroid/content/pm/PackageManager;->freeStorageAndNotify(JLandroid/content/pm/IPackageDataObserver;)",
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;": [
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->freeStorage(JLandroid/content/IntentSender;)",
        "Landroid/content/pm/IPackageManager$Stub$Proxy;->freeStorageAndNotify(JLandroid/content/pm/IPackageDataObserver;)",
    ],
},
"android.permission.ASEC_ACCESS": {
    "Landroid/os/storage/IMountService$Stub$Proxy;": [
        "Landroid/os/storage/IMountService$Stub$Proxy;->getSecureContainerList(L;)",
        "Landroid/os/storage/IMountService$Stub$Proxy;->getSecureContainerPath(Ljava/lang/String;)",
        "Landroid/os/storage/IMountService$Stub$Proxy;->isSecureContainerMounted(Ljava/lang/String;)",
    ],
},
"The": {
    "Landroid/app/Activity;": [
        "Landroid/app/Activity;->sendBroadcast(Landroid/content/Intent;)",
        "Landroid/app/Activity;->sendOrderedBroadcast(Landroid/content/Intent;Ljava/lang/String;)",
        "Landroid/app/Activity;->startActivity(Landroid/content/Intent;)",
        "Landroid/app/Activity;->startActivityForResult(Landroid/content/Intent;I)",
        "Landroid/app/Activity;->startActivityFromChild(Landroid/app/Activity;Landroid/content/Intent;I)",
        "Landroid/app/Activity;->startActivityIfNeeded(Landroid/content/Intent;I)",
    ],
    "Landroid/content/ContextWrapper;": [
        "Landroid/content/ContextWrapper;->sendBroadcast(Landroid/content/Intent;)",
        "Landroid/content/ContextWrapper;->sendOrderedBroadcast(Landroid/content/Intent;Ljava/lang/String;)",
        "Landroid/content/ContextWrapper;->startActivity(Landroid/content/Intent;)",
        "Landroid/content/ContextWrapper;->startService(Landroid/content/Intent;)",
    ],
    "Landroid/app/Service;": [
        "Landroid/app/Service;->sendBroadcast(Landroid/content/Intent;)",
        "Landroid/app/Service;->sendOrderedBroadcast(Landroid/content/Intent;Ljava/lang/String;)",
        "Landroid/app/Service;->startActivity(Landroid/content/Intent;)",
        "Landroid/app/Service;->startService(Landroid/content/Intent;)",
    ],
    "Landroid/content/Context;": [
        "Landroid/content/Context;->sendBroadcast(Landroid/content/Intent;)",
        "Landroid/content/Context;->sendOrderedBroadcast(Landroid/content/Intent;Ljava/lang/String;)",
        "Landroid/content/Context;->startActivity(Landroid/content/Intent;)",
        "Landroid/content/Context;->startService(Landroid/content/Intent;)",
    ],
},
"android.permission.SET_ORIENTATION": {
    "Landroid/view/IWindowManager$Stub$Proxy;": [
        "Landroid/view/IWindowManager$Stub$Proxy;->setRotation(IZI)",
    ],
},
"android.permission.SET_ACTIVITY_WATCHER": {
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->profileControl(Ljava/lang/String;ZLjava/lang/String;Landroid/os/ParcelFileDescriptor;)",
        "Landroid/app/IActivityManager$Stub$Proxy;->setActivityController(Landroid/app/IActivityController;)",
    ],
},
"android.permission.READ_SMS": {
    "Landroid/provider/Telephony$Sms$Sent;": [
        "Landroid/provider/Telephony$Sms$Sent;->addMessage(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Long;)",
    ],
    "Landroid/provider/Telephony$Mms;": [
        "Landroid/provider/Telephony$Mms;->query(Landroid/content/ContentResolver;L[Ljava/lang/String;;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/provider/Telephony$Mms;->query(Landroid/content/ContentResolver;L[Ljava/lang/String;;)",
    ],
    "Landroid/provider/Telephony$Sms;": [
        "Landroid/provider/Telephony$Sms;->query(Landroid/content/ContentResolver;L[Ljava/lang/String;;Ljava/lang/String;Ljava/lang/String;)",
        "Landroid/provider/Telephony$Sms;->query(Landroid/content/ContentResolver;L[Ljava/lang/String;;)",
    ],
    "Landroid/provider/Telephony$Sms$Draft;": [
        "Landroid/provider/Telephony$Sms$Draft;->addMessage(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Long;)",
    ],
    "Landroid/provider/Telephony$Threads;": [
        "Landroid/provider/Telephony$Threads;->getOrCreateThreadId(Landroid/content/Context;Ljava/lang/String;)",
        "Landroid/provider/Telephony$Threads;->getOrCreateThreadId(Landroid/content/Context;Ljava/util/Set;)",
    ],
    "Landroid/provider/Telephony$Sms$Inbox;": [
        "Landroid/provider/Telephony$Sms$Inbox;->addMessage(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Long;Z)",
    ],
},
"android.permission.VIBRATE": {
    "Landroid/os/Vibrator;": [
        "Landroid/os/Vibrator;->cancel(L;)",
        "Landroid/os/Vibrator;->vibrate(L[J;I)",
        "Landroid/os/Vibrator;->vibrate(J)",
    ],
    "Landroid/app/NotificationManager;": [
        "Landroid/app/NotificationManager;->notify(ILandroid/app/Notification;)",
        "Landroid/app/NotificationManager;->notify(Ljava/lang/String;ILandroid/app/Notification;)",
    ],
    "Landroid/os/IVibratorService$Stub$Proxy;": [
        "Landroid/os/IVibratorService$Stub$Proxy;->cancelVibrate(Landroid/os/IBinder;)",
        "Landroid/os/IVibratorService$Stub$Proxy;->vibrate(JLandroid/os/IBinder;)",
        "Landroid/os/IVibratorService$Stub$Proxy;->vibratePattern(L[J;ILandroid/os/IBinder;)",
    ],
},
"android.permission.GLOBAL_SEARCH": {
    "Landroid/server/search/Searchables;": [
        "Landroid/server/search/Searchables;->buildSearchableList(L;)",
        "Landroid/server/search/Searchables;->findGlobalSearchActivity(L;)",
    ],
},
"android.permission.PACKAGE_USAGE_STATS": {
    "Lcom/android/internal/app/IUsageStats$Stub$Proxy;": [
        "Lcom/android/internal/app/IUsageStats$Stub$Proxy;->getAllPkgUsageStats(L;)",
        "Lcom/android/internal/app/IUsageStats$Stub$Proxy;->getPkgUsageStats(LComponentName;)",
    ],
},
"android.permission.SET_ALWAYS_FINISH": {
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->setAlwaysFinish(Z)",
    ],
},
"android.permission.BROADCAST_STICKY": {
    "Landroid/app/Service;": [
        "Landroid/app/Service;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/Service;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/Service;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/view/ContextThemeWrapper;": [
        "Landroid/view/ContextThemeWrapper;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/view/ContextThemeWrapper;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/view/ContextThemeWrapper;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/content/Context;": [
        "Landroid/content/Context;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/content/Context;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/content/Context;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/inputmethodservice/AbstractInputMethodService;": [
        "Landroid/inputmethodservice/AbstractInputMethodService;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/inputmethodservice/AbstractInputMethodService;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/inputmethodservice/AbstractInputMethodService;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/ListActivity;": [
        "Landroid/app/ListActivity;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/ListActivity;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/ListActivity;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/ExpandableListActivity;": [
        "Landroid/app/ExpandableListActivity;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/ExpandableListActivity;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/ExpandableListActivity;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/TabActivity;": [
        "Landroid/app/TabActivity;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/TabActivity;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/TabActivity;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/ActivityGroup;": [
        "Landroid/app/ActivityGroup;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/ActivityGroup;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/ActivityGroup;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;": [
        "Landroid/app/IActivityManager$Stub$Proxy;->unbroadcastIntent(Landroid/app/IApplicationThread;Landroid/content/Intent;)",
    ],
    "Landroid/app/ContextImpl;": [
        "Landroid/app/ContextImpl;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/ContextImpl;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/ContextImpl;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/speech/RecognitionService;": [
        "Landroid/speech/RecognitionService;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/speech/RecognitionService;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/speech/RecognitionService;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/IntentService;": [
        "Landroid/app/IntentService;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/IntentService;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/IntentService;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/AliasActivity;": [
        "Landroid/app/AliasActivity;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/AliasActivity;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/AliasActivity;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/backup/BackupAgent;": [
        "Landroid/app/backup/BackupAgent;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/backup/BackupAgent;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/backup/BackupAgent;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/FullBackupAgent;": [
        "Landroid/app/FullBackupAgent;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/FullBackupAgent;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/FullBackupAgent;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/backup/BackupAgentHelper;": [
        "Landroid/app/backup/BackupAgentHelper;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/backup/BackupAgentHelper;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/backup/BackupAgentHelper;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/content/ContextWrapper;": [
        "Landroid/content/ContextWrapper;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/content/ContextWrapper;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/content/ContextWrapper;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/accessibilityservice/AccessibilityService;": [
        "Landroid/accessibilityservice/AccessibilityService;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/accessibilityservice/AccessibilityService;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/accessibilityservice/AccessibilityService;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/service/urlrenderer/UrlRendererService;": [
        "Landroid/service/urlrenderer/UrlRendererService;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/service/urlrenderer/UrlRendererService;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/service/urlrenderer/UrlRendererService;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/service/wallpaper/WallpaperService;": [
        "Landroid/service/wallpaper/WallpaperService;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/service/wallpaper/WallpaperService;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/service/wallpaper/WallpaperService;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/Application;": [
        "Landroid/app/Application;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/Application;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/Application;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
        "Landroid/app/Application;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/app/Activity;": [
        "Landroid/app/Activity;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/Activity;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/app/Activity;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/content/MutableContextWrapper;": [
        "Landroid/content/MutableContextWrapper;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/content/MutableContextWrapper;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/content/MutableContextWrapper;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/accounts/GrantCredentialsPermissionActivity;": [
        "Landroid/accounts/GrantCredentialsPermissionActivity;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/accounts/GrantCredentialsPermissionActivity;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/accounts/GrantCredentialsPermissionActivity;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
    "Landroid/accounts/AccountAuthenticatorActivity;": [
        "Landroid/accounts/AccountAuthenticatorActivity;->removeStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/accounts/AccountAuthenticatorActivity;->sendStickyBroadcast(Landroid/content/Intent;)",
        "Landroid/accounts/AccountAuthenticatorActivity;->sendStickyOrderedBroadcast(Landroid/content/Intent;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)",
    ],
},
"android.permission.MOUNT_UNMOUNT_FILESYSTEMS": {
    "Landroid/os/storage/IMountService$Stub$Proxy;": [
        "Landroid/os/storage/IMountService$Stub$Proxy;->getStorageUsers(Ljava/lang/String;)",
        "Landroid/os/storage/IMountService$Stub$Proxy;->mountVolume(Ljava/lang/String;)",
        "Landroid/os/storage/IMountService$Stub$Proxy;->setUsbMassStorageEnabled(Z)",
        "Landroid/os/storage/IMountService$Stub$Proxy;->unmountVolume(Ljava/lang/String;Z)",
    ],
    "Landroid/os/IMountService$Stub$Proxy;": [
        "Landroid/os/IMountService$Stub$Proxy;->mountMedi(Landroid/os/IMountService$Stub$Proxy/mountMedi;)",
        "Landroid/os/IMountService$Stub$Proxy;->unmountMedi(Landroid/os/IMountService$Stub$Proxy/unmountMedi;)",
    ],
    "Landroid/os/storage/StorageManager;": [
        "Landroid/os/storage/StorageManager;->disableUsbMassStorage(L;)",
        "Landroid/os/storage/StorageManager;->enableUsbMassStorage(L;)",
    ],
},
}
