(this.webpackJsonpsecdash1=this.webpackJsonpsecdash1||[]).push([[2],{13:function(e,n,t){"use strict";n.a={defaultPath:"/auth/signin",homePath:"/dashboard",layout:"vertical",preLayout:null,collapseMenu:!1,layoutType:"menu-light",navIconColor:!1,headerBackColor:"header-default",navBackColor:"navbar-default",navBrandColor:"brand-default",navBackImage:!1,rtlLayout:!1,navFixedLayout:!0,headerFixedLayout:!1,boxLayout:!1,navDropdownIcon:"style1",navListIcon:"style1",navActiveListColor:"active-default",navListTitleColor:"title-default",navListTitleHide:!1,configBlock:!1,layout6Background:"linear-gradient(to right, #A445B2 0%, #D41872 52%, #FF0066 100%)",layout6BackSize:""}},19:function(e,n,t){"use strict";var a=t(0),r=t.n(a);n.a=function(){return r.a.createElement("div",{className:"loader-bg"},r.a.createElement("div",{className:"loader-track"},r.a.createElement("div",{className:"loader-fill"})))}},22:function(e,n,t){"use strict";n.a=function(e){return e.children}},36:function(e,n,t){e.exports=t(47)},47:function(e,n,t){"use strict";t.r(n);var a=t(0),r=t.n(a),i=t(23),c=t.n(i),o=t(14),u=t(24),l=t(52),s=t(9),d=t(10),m=t(12),f=t(11),p=t(49),h=t(53),b=t(32),v=t.n(b),O=(t(45),t(19)),g=t(22),E=t(48),y=function(e){Object(m.a)(t,e);var n=Object(f.a)(t);function t(){return Object(s.a)(this,t),n.apply(this,arguments)}return Object(d.a)(t,[{key:"componentDidUpdate",value:function(e){this.props.location!==e.location&&window.scrollTo(0,0)}},{key:"render",value:function(){return this.props.children}}]),t}(r.a.Component),L=Object(E.a)(y),j=[{path:"/auth/signup",exact:!0,name:"Signup 1",component:r.a.lazy((function(){return Promise.all([t.e(0),t.e(1),t.e(10)]).then(t.bind(null,204))}))},{path:"/auth/signin",exact:!0,name:"Signin 1",component:r.a.lazy((function(){return Promise.all([t.e(0),t.e(1),t.e(9)]).then(t.bind(null,205))}))}],k=v()({loader:function(){return Promise.all([t.e(0),t.e(4),t.e(6)]).then(t.bind(null,206))},loading:O.a}),T=function(e){Object(m.a)(t,e);var n=Object(f.a)(t);function t(){return Object(s.a)(this,t),n.apply(this,arguments)}return Object(d.a)(t,[{key:"render",value:function(){var e=j.map((function(e,n){return e.component?r.a.createElement(p.a,{key:n,path:e.path,exact:e.exact,name:e.name,render:function(n){return r.a.createElement(e.component,n)}}):null}));return r.a.createElement(g.a,null,r.a.createElement(L,null,r.a.createElement(a.Suspense,{fallback:r.a.createElement(O.a,null)},r.a.createElement(h.a,null,e,r.a.createElement(p.a,{path:"/",component:k})))))}}]),t}(a.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var C=t(17),S=t(5),w=t(6),x=t(13),A=Object(S.a)({isOpen:[],isTrigger:[]},x.a,{isFullScreen:!1}),N=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:A,n=arguments.length>1?arguments[1]:void 0,t=[],a=[];switch(n.type){case w.b:return Object(S.a)({},e,{collapseMenu:!e.collapseMenu});case w.c:if("sub"===n.menu.type){a=e.isOpen;var r=(t=e.isTrigger).indexOf(n.menu.id);r>-1&&(a=a.filter((function(e){return e!==n.menu.id})),t=t.filter((function(e){return e!==n.menu.id}))),-1===r&&(a=[].concat(Object(C.a)(a),[n.menu.id]),t=[].concat(Object(C.a)(t),[n.menu.id]))}else{a=e.isOpen;var i=e.isTrigger.indexOf(n.menu.id);t=-1===i?[n.menu.id]:[],a=-1===i?[n.menu.id]:[]}return Object(S.a)({},e,{isOpen:a,isTrigger:t});case w.g:return Object(S.a)({},e,{isOpen:a,isTrigger:t});case w.f:if("sub"===n.menu.type){a=e.isOpen;var c=(t=e.isTrigger).indexOf(n.menu.id);return c>-1&&(a=a.filter((function(e){return e!==n.menu.id})),t=t.filter((function(e){return e!==n.menu.id}))),Object(S.a)({},e,{isOpen:a,isTrigger:t})}return Object(S.a)({},e);case w.d:return Object(S.a)({},e,{isFullScreen:!e.isFullScreen});case w.e:return Object(S.a)({},e,{isFullScreen:!1});case w.a:return Object(S.a)({},e,{layout:n.layout});default:return e}},B=Object(o.b)(N),F=r.a.createElement(u.a,{store:B},r.a.createElement(l.a,{basename:x.a.basename},r.a.createElement(T,null)));c.a.render(F,document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))},6:function(e,n,t){"use strict";t.d(n,"b",(function(){return a})),t.d(n,"c",(function(){return r})),t.d(n,"d",(function(){return i})),t.d(n,"e",(function(){return c})),t.d(n,"a",(function(){return o})),t.d(n,"g",(function(){return u})),t.d(n,"f",(function(){return l}));var a="COLLAPSE_MENU",r="COLLAPSE_TOGGLE",i="FULL_SCREEN",c="FULL_SCREEN_EXIT",o="CHANGE_LAYOUT",u="NAV_CONTENT_LEAVE",l="NAV_COLLAPSE_LEAVE"}},[[36,3,5]]]);
//# sourceMappingURL=main.b24fb810.chunk.js.map